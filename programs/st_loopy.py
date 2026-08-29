
import sys
from pathlib import Path

sys.path.insert(0, Path.cwd().as_posix())

from src.CLIUI import CLIUI as cli
from src.KeyWord import KeyWord
from src.Splitter import Splitter
from src.datahandler import DBHandler as dbh


class stloopy:

    delm = "x"
    game = {"width":0, "height":0, "contig":0, "noncontig":0}
    data = {"width":0, "height":0, "contig":0, "noncontig":0}
    @classmethod
    def __init__(self):
        cli(history_file = ".st_loopy.rc")

        KeyWord.set_default(self.parse_str)

        KeyWord.new(["help"], self.helpme, FLAGS = KeyWord.NO_ARGS)
        KeyWord.new(["quit"], self.quit, FLAGS = KeyWord.NO_ARGS)
        KeyWord.new(["print", "config"], self.print_config, KeyWord.NO_ARGS)
        KeyWord.new(["print", "games"], self.print_data)
        KeyWord.new(["read", "data"], self.read_data)
        KeyWord.new(["set", "prompt"], self.set_prompt)
        KeyWord.new(["set", "file"], self.set_csv_file_name)
        KeyWord.new(["set", "delim"], self.set_delm)
        KeyWord.new(["set", "game"], self.set_game)
        KeyWord.new(["write"], dbh.fwrite_data, FLAGS = KeyWord.NO_ARGS)
        KeyWord.new(["undo"], dbh.undo_data, FLAGS = KeyWord.NO_ARGS)
        KeyWord.new(["define"], self.define)



        Splitter.new_delm("\"", "\"")
        Splitter.new_delm("{", "}", Splitter.DISCARD_DELMS)
        Splitter.new_delm("'", "'")
        Splitter.new_delm("[", "]", Splitter.DISCARD_DELMS)

        Splitter.add_spacer(",")
        Splitter.add_spacer(";")

        
        dbh.set_fields(["width", "height", "contig", "noncontig"])


    def helpme():
        print("help             This help.")
        print("print")
        print("      games                  Print out the games that have been played.")
        print("            -n                   The last n games played.")
        print("            span n               If the number of games is large, then ")
        print("                                 span the entire list only printing n  ")
        print("                                 number of games until end.")
        print("      config                 Print settings.")
        print("set                          Sets configuration settings.")
        print("    game WxH                 Sets the width and height of the game data to be ")
        print("    game W H                 Same as set game WxH.")
        print("    file name                Sets file to name.")
        print("    prompt p                 Sets prompt to string p.")
        print("    delim n                  Sets the delimiter for entering data for the file.")
        print("read data                    Loads all data stored in file.")
        print("          fieldlist[numbers]   Reads only the fields given that    ")
        print("                               contain numbers.")
        print("write                        Write data to file.")
        print("undo                         Removes the last data that was inserted.")
        print("quit                         Exit program.")
        print("\n\n")
        print("define field n               Set field as n. Then the rest of the data doesn't")
        print("                                need to be entered.")
        print("CxN                          Game data that is stored til written to file.")
    

    @classmethod
    def set_game(self, ARGS):
        if ARGS == None:
            return()
        C = None
        if len(ARGS) == 2:
            if ARGS[0].isnumeric() and ARGS[1].isnumeric():
                C = [int(ARGS[0]), int(ARGS[1]) ]
        elif len(ARGS) == 1:
            C = ARGS[0].split("x")
            if C[0].isnumeric() and C[1].isnumeric():
                C = [int(C[0]), int(C[1]) ]

        if C != None:
            self.game = { "width":C[0], "height":C[1], "contig":0, "noncontig":0}
#             self.game["width"]  = C[0]
#             self.game["height"] = C[1]
        




    def quit():
        cli.write_history() 
        quit()


    @classmethod
    def print_data(self, ARGS):
        span = False

        c = 0

        if dbh.data == None:
            return()
        if ARGS != None:
            if len(ARGS) == 1:
                if ARGS[0][0] == "-":
                    if ARGS[0][1:].isnumeric():
                        c = -1 * int(ARGS[0][1:])
            else:
                if len(ARGS) == 2:
                    if (ARGS[0] == "span") and (ARGS[1].isnumeric()):
                        span = True   
                        c = int(ARGS[1]) 
                    else:
                        return()

        print("width   : height : contig : noncontig") 
        if c < 0:
            for d in dbh.data[c:]:
                print(f"  {d['width']:2}    :  {d['height']:2}     :  {d['contig']:2}    :  {d['noncontig']:2}")
            return()

        if span == True:
            
            x = 0
            y = c
            while True:
                for d in dbh.data[x:y]:
                    print(f"  {d['width']:2}    :  {d['height']:2}    :  {d['contig']:2}    :  {d['noncontig']:2}")
                if cli.ynmessage("Press any key to continue. n to quit.", ANYKEY = True) == False:
                    break
                x = y 
                y+=c   
                if x > len(dbh.data):
                    break
        else:
            
            for d in dbh.data:
                print(f"  {d['width']:2}    :  {d['height']:2}    :  {d['contig']:2}    :  {d['noncontig']:2}")



    @classmethod
    def run(self):
        while True:
            C = cli.input()
            args = Splitter.split(C)

            KeyWord.execute(args)

   
    @classmethod
    def parse_str(self, ARGS):
        if ARGS == None:
            return()
        if len(ARGS) == 1:
            game = ARGS[0].split(self.delm)
            if len(game)==1:
                return()
            if game[0].isnumeric() and game[1].isnumeric:
                self.game["contig"] = int(game[0])
                self.game["noncontig"] = int(game[1])
                dbh.add_data(self.game)
        if len(ARGS) == 2:
            if ARGS[0].isnumeric() and ARGS[1].isnumeric():
                self.game["contig"] = int(ARGS[0])
                self.game["noncontig"] = int(ARGS[1])
                dbh.add_data(self.game)
            
        print("String that was passed is : ", ARGS)

    def set_prompt(ARGS):
        if ARGS == None:
            return()
        
        cli.prompt = ARGS[0][1:-1]
             
    @classmethod
    def print_config(self):
        print(f"prompt         = \"{cli.prompt}\"")
        print(f"filename       = {dbh.filename}")
        print(f"Data delimiter = \"{self.delm}\"")

        print(f"Current game   = {self.game['width']}x{self.game['height']}")
        for f in dbh.fieldnames:
            if f == "width":
                header = "fields         = "
            else:
                header = "                 "

            msg = f"{header}{f:10} : {self.game[f]}"

            print(msg)

        print(f"History file   = {cli.historyrc}")

            

    def set_csv_file_name(ARGS):
        if ARGS == None:
            return()

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
                    dbh.filename = filename 
                    dbh.fwrite_data(header = True)
    
                except:
                    print("Can not create file.")
                    
            return(False)

    @classmethod
    def set_delm(self, ARGS):   
        if (ARGS == None) or (len(ARGS) > 1):
            return()
        if len(ARGS[0]) > 1:
            return()
        self.delm = ARGS[0]


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

        if (ARGS == None) or (len(ARGS) != 2):
            return()

        for f in dbh.fieldnames:
            if ARGS[0] == f:
                if ARGS[1].isnumeric():
                    self.data[ARGS[0]] = int(ARGS[1])

    @classmethod
    def read_data(self, ARGS):
        if ARGS == None:            # Read all data.
            dbh.fread_data(None)
        else:
            if len(ARGS) %2 == 0:
                A = [ [ ARGS[c*2], ARGS[c*2+1].split(",") ] for c in range(len(ARGS)//2) ]
                for a in A:
                    for x in range(len(a[1])):
                        if not a[1][x].isnumeric():
                            return()
                        else:
                            a[1][x] = int(a[1][x])
                dbh.fread_data(A)

                
     
        print(dbh.data)
       

        

stl = stloopy()

stl.run()

