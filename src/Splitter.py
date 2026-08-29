



#  Splitter             Extra functionality for splitting strings.


#  delimiter usage...

#   "#", 1, "", 0, 0            Will return everything after ",".

#   "{", 1, "}", 1, DISCARD_DELIMITER   Will return everything between {, }, a null character
#                                       if everything is spaces. 

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
                            tail -= 1
                            head += d[1]
                            x += tail + d[3]
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

#     @classmethod
#     def split(self, instr):
# 
#         A = []
# 
#         x = 0
# 
#         tail = -1
# 
#         while x < len(instr):
#             for sp in self.spacers:
#                 if sp == instr[x]:
#                     sp = ""
#                     break;
#             if sp == "":
#                 x+=1
#                 continue
# 
#             pos = [0,0]
#            
#             for d in self.delms:
#                 if d[0] == instr[x:x+d[1]]:
#                     tail = instr[x+d[1]:].find(d[2])
#                     if tail < 0:
#                         d = None
#                     else:
#                         tail = tail + x + d[1]
# 
#                         if d[4] & self.DISCARD_STRING:
#                             tail = tail + d[3] 
#                             break
# 
#                         if d[4] & self.DISCARD_DELMS:
#                             pos = [x+d[1], tail]
#                         else:
#                             pos = [x, tail+d[3]]
#                         x = x + d[3]
#                         print(pos, "   ", x, ":", tail)
#                     break
#                 else:
#                     d = None
# 
#             if d == None:
#                 tail = x
#                 while True:
#                     tail+=1
#                     if tail >= len(instr):
#                         pos = [x,tail]
#                         break
#                     for sp in self.spacers:
#                         if instr[tail] == sp:
#                             pos=[x, tail]
#                             sp = ""
#                             break
#                     if sp == "":
#                         break
# 
#             x = tail+1
# 
#             if pos[0] != pos[1]:
#                
#                 A.append(instr[pos[0]:pos[1]])
# 
#         return(A)

Splitter.new_delm("\"", "\"")
Splitter.new_delm("[", "]")
Splitter.new_delm("{", "}")
Splitter.new_delm("'", "'")
Splitter.new_delm("##", "##", flags = Splitter.DISCARD_STRING)

while True:
    a = input("Input a string $ ")
    if a == "quit":
        break
    S = Splitter.split(a)
    print(S)
