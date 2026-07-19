

KEEP_DELMS     = 0
DISCARD_DELMS  = 1
DISCARD_STRING = 2

D_HEAD     = 0
D_HEAD_LEN = 1
D_TAIL     = 2
D_TAIL_LEN = 3
D_FLAGS    = 4

class Str2Array:

    delms = []


    @classmethod
    def new_delm(self, h, t, flags = 0):

        self.delms.append([h, len(h), t, len(t), flags])




    @classmethod
    def split(self, instr):

        Array = []

        if len(instr) == 0:
            return([])          # Return an empty list if instr is empty

        x = 0 
        a = 0
        c = False

        head = -1
        tail = -1


        while x < len(instr):
            while instr[x] == " ":          # Remove white spaces.
                x+=1
            if head < 0:
                head = x                        # Set head.
            for d in self.delms:
                if d[D_HEAD] == instr[x:x+d[D_HEAD_LEN]]:
                    if head != x:                               # If delm is within string, do not read delms.
                        tail = x - 1                            # do not set c to True.
                        x = tail
                        break
                    c = True                                    # set c to True for finding delm tail.
                    break

            if c == True:                                       # find tail
                tail = instr[head+d[D_HEAD_LEN]:].find(d[D_TAIL])       # Get tail, else -1
                c = False
                if tail > 0:
                    if d[D_FLAGS] & DISCARD_STRING:                     # Skip string and tail end.
                        x = tail + d[D_HEAD_LEN] + d[D_TAIL_LEN] + head 
                        tail = -1
                        head = -1
                    elif d[D_FLAGS] & DISCARD_DELMS:
                        head = head + d[D_HEAD_LEN] 
                        tail = head + tail 
                        x = tail + d[D_TAIL_LEN]
                        tail = tail -1
                    else:   #d[D_FLAGS] & KEEP_DELMS:
                        tail = head + tail +d[D_HEAD_LEN] + d[D_TAIL_LEN]  
                        x = tail
                        tail = tail-1
            else:
                x+=1

            if (tail < 0) and (head >= 0 ):                       # If tail wasn't found, test for space character.
                if (instr[x] == " "):                           # Then set tail for adding a non-delm string
                    tail = x - 1

            if tail > 0:                                        # If tail was found.
                Array.append(instr[head:tail+1])
                head = -1
                tail = -1


        return(Array)


Str2Array.new_delm("[", "]", KEEP_DELMS)
Str2Array.new_delm("(", ")", KEEP_DELMS)
Str2Array.new_delm("{", "}", DISCARD_DELMS)
Str2Array.new_delm("\"", "\"", KEEP_DELMS)
Str2Array.new_delm("'", "'", KEEP_DELMS)
Str2Array.new_delm("/*", "*/", DISCARD_STRING)

