


class Keyword:
   
    default = False
    keys = ["default", None, 0, []]


    @classmethod
    def exec(self, sl):
        K = self.getkey(sl)
        
        if K[0] == [] and self.default == True:
            self.keys[1](K[1])
        else:
            K[0][2](K[1])


    @classmethod
    def getkey(self, sl):

        searchkey = self.keys[3]
        lastkey = [] 
        if searchkey == []:
            return([[], sl])

        C = False
        x = 0
        while x < len(sl):
            for key in searchkey:
                if key[0] == sl[x]:
                    x+=1
                    lastkey = key
                    searchkey = key[3]
                    C = True
                    break
            if C == False:
                break
            else:
               C = False


        return([lastkey, sl[x:]])


    @classmethod
    def addkey(self, sl, func, flags=0):
       
        while True: 
            K = self.getkey(sl)
            if K[1] == []:
                break

            if K[0] == []:
                self.keys[3].append([K[1][0],None, 0, []])
            else:
                K[0][3].append([K[1][0], None, 0, []])


        K[0][1] = func;
        K[0][2] = flags;


