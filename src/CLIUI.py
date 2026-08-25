

import readline

from pathlib import Path


class CLIUI:

    history_dir = ""
    history_file = ""
    historyrc = ""

    prompt = "input $ "

    initialized = False

    @classmethod
    def __init__(self, history_file = "", history_dir=""):

        if (history_file == "") and (self.history_file == ""):
            print("No history file to load. All history will be during this instance instead.")
            return()
        
        self.history_file = history_file
     
        if history_dir=="":
            self.history_dir = Path.home().as_posix()
        else:
            self.history_dir = history_dir

        self.historyrc = self.history_dir + "/" + self.history_file

        self.initialized = True

        if Path.exists(self.history_file):          
            readline.read_history_file(self.historyrc)
        else:                                           # Go ahead and write a history file.
                                                        # just to make sure it's there.
            readline.write_history_file(self.historyrc)


    @classmethod
    def __del__(self):
        if self.initialized == True:
            self.write_history()

    @classmethod
    def write_history(self):

        if self.historyrc != "":
            readline.write_history_file(self.historyrc)

    @classmethod
    def input(self):
        return(input(self.prompt))

    def ynmessage(instr):
        yn = input(instr)
        yn = yn.lower()
        if (yn == "y") or (yn == "yes"):
            return(True)
        else:
            return(False)


