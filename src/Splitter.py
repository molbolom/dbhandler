



#  Splitter             Extra functionality for splitting strings.


#  delimiter usage...

#   "#", 1, "", 0, 0            Will return everything after ",".

#   "{", 1, "}", 1, DISCARD_DELIMITER   Will return everything between {, }, a null character
#                                       if everything is spaces. 

#############################################################################################
#
#   TODO            TODO            TODO            TODO    
#
#       Add a routine and flag for splitting a string via code like statements.
#
#       this = something;   would become [this, something]
#
#       this = something; andthis = somethingelse;   would become [this, something], [andthis, somethingelse]
#
#############################################################################################

class Splitter:


    delimiters = []

    spacers    = [" "]

    DISCARD_STRING = 1

    DISCARD_DELIMITER = 2

    USE_AS_SPACE = 3

    delms = []
    DISCARD_DELMS = 2


    @classmethod
    def new_delm(self, head, tail, flags=0):
        self.delms.append([head, len(head), tail, len(tail), flags])

    @classmethod
    def add_spacer(self, spc):
        if len(spc) > 1:
            return()
        self.spacers.append(spc)


    @classmethod
    def split(self, instr):
        A = []

        x = 0

        head = -1
        tail = -1
        discardstring = False


        while x < len(instr):
            if head < 0:
                head = x                    # Start read of string.

            for d in self.delms:
                if d[0] == instr[x:x+d[1]]:                 # Found head.
                    tail = instr[x+d[1]:].find(d[2])
                    if tail < 0:                            # Tail wasn't found, read normal string.
                        break
                    if head != x:                           # Delm is against string.
                        tail=x                              # Set tail to last character.
                        x-=1                                # Move x to previous character.
                        break
                    else:
                        if d[4] & self.DISCARD_STRING:
                            discardstring = True
                        if d[4] & self.DISCARD_DELMS:
                            tail += x + d[1]  
                            head += d[1]
                            x = tail + d[3]
                            break 
                        else:
                            tail += x + d[1] + d[3] 
                            x = tail
                            break

            if tail < 0:
                for sp in self.spacers:                     # Test for space characters. Non-readable characters.
                    if instr[x] == sp:
                        tail = x
                        break
            if tail > 0:
                if discardstring == False:
                    A.append(instr[head:tail])
                tail = -1
                head = -1
                discardstring = False
            x+=1
        if head != -1:
            A.append(instr[head:x])

        return(A)

