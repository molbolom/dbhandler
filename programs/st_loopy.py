
import sys
from pathlib import Path

sys.path.insert(0, Path.cwd().as_posix())

from src.CLIUI import CLIUI as cli
from src.KeyWord import KeyWord
from src.Splitter import Splitter
from src.datahandler import DBHandler as dbh


class stloopy:

    @classmethod
    def __init__(self):
        cli(history_file = ".st_loopy.rc")

        KeyWord.set_default(self.parse_str)

        KeyWord.new(["help"], self.helpme, FLAGS = KeyWord.NO_ARGS)
        KeyWord.new(["quit"], self.quit, FLAGS = KeyWord.NO_ARGS)
        KeyWord.new(["print", "config"], self.print_config, KeyWord.NO_ARGS)
        KeyWord.new(["set", "prompt"], self.set_prompt)
        KeyWord.new(["set", "file"], self.set_csv_file_name)
        KeyWord.new(["set", "fields"], self.set_fieldnames)

        Splitter.new_delm("\"", "\"")
        Splitter.new_delm("{", "}", Splitter.DISCARD_DELIMITER)
        Splitter.new_delm("'", "'")

        Splitter.add_spacer(",")
        Splitter.add_spacer(";")

    def helpme():
        print("help             This help.")
        print("print")
        print("      data n     Print n number of stored data until q is pressed.")
        print("      config     Print settings.")
        print("set              Sets configuration settings.")
        print("    file name    Sets file to name.")
        print("    fields n     Sets fields to n.")
        print("                    n is either a list of field names, or an integer")
        print("                    for the length of the fields if field names is")
        print("                    not used.")
        print("    prompt p     Sets prompt to string p.")
        print("write            Write data to file.")
        print("undo             Removes the last data that was inserted.")
        print("quit             Exit program.")

    def quit():
        cli.write_history() 
        quit()

    @classmethod
    def run(self):
        while True:
            C = cli.input()
            args = Splitter.split(C)

            KeyWord.execute(args)

    @classmethod
    def parse_str(self, ARGS):
        print("String that was passed is : ", ARGS)

    def set_prompt(ARGS):
        
        cli.prompt = ARGS[0][1:-1]
             
    @classmethod
    def print_config(self):
        print(f"prompt = \"{cli.prompt}\"")
        print(f"filename = {dbh.filename}")

    def set_csv_file_name(ARGS):

        if len(ARGS) == 1:
            if ARGS[0][-3:] != "csv":
                print("File is not a csv file.")
                return(False)
            filename = ARGS[0]
        else:
            return(False)

        if Path.exists(filename) == True:
            dbh.filename = filename
            return(True)
        else:
            yn = cli.ynmessage("File doesn't exist. Do you want to create it? [ y or n ] ")
            if yn == True:
                try:
                    with open(filename, "w") as cf:
                        pass
    
                    dbh.filename = filename 
                except:
                    print("Can not create file.")
                    
            return(False)

       
    def set_fieldnames(ARGS):
        print(ARGS)
        

stl = stloopy()

stl.run()

