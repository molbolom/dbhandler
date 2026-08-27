
import sys
from pathlib import Path

sys.path.insert(0, Path.cwd().as_posix())

from src.CLIUI import CLIUI as cli
from src.KeyWord import KeyWord
from src.Splitter import Splitter
from src.datahandler import DBHandler as dbh


class stloopy:

    delm = "x"

    data = {"width":0, "height":0, "contig":0, "noncontig":0}
    @classmethod
    def __init__(self):
        cli(history_file = ".st_loopy.rc")

        KeyWord.set_default(self.parse_str)

        KeyWord.new(["help"], self.helpme, FLAGS = KeyWord.NO_ARGS)
        KeyWord.new(["quit"], self.quit, FLAGS = KeyWord.NO_ARGS)
        KeyWord.new(["print", "config"], self.print_config, KeyWord.NO_ARGS)
        KeyWord.new(["set", "prompt"], self.set_prompt)
        KeyWord.new(["set", "file"], self.set_csv_file_name)
        KeyWord.new(["set", "delim"], self.set_delm)
        KeyWord.new(["set", "game"], self.set_game)
        KeyWord.new(["write"], dbh.fwrite_data, FLAGS = KeyWord.NO_ARGS)
        KeyWord.new(["undo"], dbh.undo_data, FLAGS = KeyWord.NO_ARGS)
        KeyWord.new(["define"], self.define)



        Splitter.new_delm("\"", "\"")
        Splitter.new_delm("{", "}", Splitter.DISCARD_DELIMITER)
        Splitter.new_delm("'", "'")

        Splitter.add_spacer(",")
        Splitter.add_spacer(";")

        dbh.set_fields(["width", "height", "contig", "noncontig"])


    def helpme():
        print("help             This help.")
        print("print")
        print("      data n     Print n number of stored data until q is pressed.")
        print("      config     Print settings.")
        print("set              Sets configuration settings.")
        print("    game WxH     Sets the width and height of the game data to be ")
        print("                    added to the file.")
        print("    file name    Sets file to name.")
        print("    fields n     Sets fields to n.")
        print("                    n is either a list of field names, or an integer")
        print("                    for the length of the fields if field names is")
        print("                    not used.")
        print("    prompt p     Sets prompt to string p.")
        print("    delim n      Sets the delimiter for entering data for the file.")
        print("write            Write data to file.")
        print("undo             Removes the last data that was inserted.")
        print("quit             Exit program.")
        print("\n\n")
        print("define field n   Set field as n. Then the rest of the data doesn't")
        print("                 need to be entered.")
        print("WxH CxN          Temporary data that will be written to the file.")
    

    @classmethod
    def set_game(self, ARGS):
        C = None
        if len(ARGS) == 2:
            if ARGS[0].isnumeric() and ARGS[1].isnumeric():
                C = [int(ARGS[0]), int(ARGS[1]) ]
        elif len(ARGS) == 1:
            C = ARGS[0].split("x")
            if C[0].isnumeric() and C[1].isnumeric():
                C = [int(C[0]), int(C[1]) ]

        if C != None:
            self.data["width"]  = C[0]
            self.data["height"] = C[1]
        




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
        print(f"prompt         = \"{cli.prompt}\"")
        print(f"filename       = {dbh.filename}")
        print(f"Data delimiter = \"{self.delm}\"")

        for f in dbh.fieldnames:
            if f == "width":
                header = "fields         = "
            else:
                header = "                 "

            if self.data[f] == 0:
                msg = f"{header}{f:10}"
            else:
                msg = f"{header}{f:10} : {self.data[f]}"
            print(msg)

            

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

    @classmethod
    def set_delm(self, ARGS):   
        if len(ARGS) > 1:
            return()
        if len(ARGS[0]) > 1:
            return()
        self.delm = ARGS[0]

#######################################################################
#
#           No need for set field names
#
#######################################################################

#    @classmethod
#    def set_fieldnames(self, ARGS):
#        if len(ARGS) == 1:
#            if ARGS[0].isnumeric():
#                dbh.fieldc = int(ARGS[0])
#                dbh.fieldnames = None
#                self.data = [ 0 for n in range(dbh.fieldc) ]
#
#        else:
#            dbh.fieldc = 0
#            dbh.fieldnames = [ f for f in ARGS ]
#            self.data = { fn:0 for fn in ARGS }
        

#######################################################################
#
#
#
#
#----------------------------------------------------------------------
#                           TODO
#
#
#   Need to check to ensure it writes to either a dict or an array.
#                           WHY???
#   This is for ST loopy, and I know what this does...There's no need
#   to make this universal.
#
#######################################################################

    @classmethod
    def define(self, ARGS):

        if len(ARGS) != 2:
            return()

        for f in dbh.fieldnames:
            if ARGS[0] == f:
                if ARGS[1].isnumeric():
                    self.data[ARGS[0]] = int(ARGS[1])
        
        

stl = stloopy()

stl.run()

