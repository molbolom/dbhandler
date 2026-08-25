

# keyword.py
#
#   This file contains all the keyword handling routines for the program.


KEY_NAME  = 0
KEY_FUNC  = 1
KEY_FLAGS = 2
KEY_SUBS  = 3

class KeyWord:
    
    keys = ["default", 0, 0, None]

    Default = False

    NO_ARGS = 1


    @classmethod
    def set_default(self, function):
        self.Default = True
        self.keys[KEY_FUNC] = function

    @classmethod
    def execute(self, keylist):
        A = self.get(keylist)
        if A[0] == self.keys:
            if self.Default == True:
                self.keys[KEY_FUNC](keylist)
            return() 

        if (A[0][KEY_FLAGS] & self.NO_ARGS):
            if A[1] != None:
                return()
            A[0][KEY_FUNC]()
        else:
            A[0][KEY_FUNC](A[1])


#
#   new([keyword list], function, FLAGS = )
#
    @classmethod
    def new(self, keylist, function, FLAGS = 0):
        while True:
            A = self.get(keylist)
            if A[1] == None:
                break
            if A[0][KEY_SUBS] == None:
                A[0][KEY_SUBS] = [ [ A[1][0], 0, 0, None] ]
            else:
                A[0][KEY_SUBS].append([ A[1][0], 0, 0, None ])

        A[0][KEY_FUNC] = function
        A[0][KEY_FLAGS] = FLAGS
            
            

    #   get_key( [ list of keywords ] )

    @classmethod
    def get(self, keylist):

        keys = self.keys

        x  = 0
        lx = 0
        for k in keylist:
            if keys[KEY_SUBS] == None:
                break
            for key in keys[KEY_SUBS]:
                if key[KEY_NAME] == k:
                    x+=1
                    keys = key
                    break
            if lx == x:
                break
            lx = x

        if x >= len(keylist):
            return([keys, None])
        else:
            return([keys, keylist[x:]])

                    
                



        

