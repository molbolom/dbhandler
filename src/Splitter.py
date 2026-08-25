



#  Splitter             Extra functionality for splitting strings.


#  delimiter usage...

#   "#", 1, "", 0, 0            Will return everything after ",".

#   "{", 1, "}", 1, DISCARD_DELIMITER   Will return everything between {, }, a null character
#                                       if everything is spaces. 

class Splitter:


    delimiters = []

    DISCARD_STRING = 1

    DISCARD_DELIMITER = 2

    USE_AS_SPACE = 3

    delms = []
    DISCARD_DELMS = 2


    @classmethod
    def new_delm(self, head, tail, flags=0):
        self.delms.append([head, len(head), tail, len(tail), flags])

    @classmethod
    def split(self, instr):

        A = []

        x = 0

        tail = -1

        while x < len(instr):
            if instr[x] == " ":
                x+=1
                continue

            c = False
            for d in self.delms:
                if d[0] == instr[x:x+d[1]]:
                    c = True
                    break

            if c == True:                       # Delm found
                tail = instr[x+d[1]:].find(d[2])
                if tail < 0:                    # If tail not found, reset tail.
                    c = False
                else:
                    tail += x+d[3]+1

            if c == False:                      # Read normal string.
                tail = x
                while True:
                    tail+=1
                    if tail >= len(instr):
                        break
                    elif instr[tail] == " ":
                        break

            if tail > 0:

                if d[4] & self.DISCARD_DELMS:
                    x+=d[1]
                    tail-=d[3]

                if not(d[4] & self.DISCARD_STRING):
                    A.append(instr[x:tail])

                x = tail

            x+=1

        return(A) 



