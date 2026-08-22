

import readline as InputXHistory


class inputx:

    historyfile = ""

    prompt = "Input > "

    @classmethod
    def set_history_file(self, filename):
        self.historyfile = filename

        try:
            #  Create/load file and set parameters.

            InputXHistory.read_history_file(self.historyfile)
            return(True)
        except:
            print("History file ", filename, " could not be read.")
            return(False)

    @classmethod
    def write_history_file(self):
        try:
            if self.historyfile != "":
                InputXHistory.write_history_file(self.historyfile)
        except:
            print("Can not write to ", self.historyfile, ".")


    @classmethod
    def input(self):
        return input(self.prompt)
