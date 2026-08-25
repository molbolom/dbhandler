
#   datahandler.py
#
#   Contains all the routines for handling databases. 
#
#   This is so any database can be used.


import csv

import random           # Temporary import

class DBHandler:


    filename = ""


                    # If fieldnames == None, then only use fieldc.

    fieldnames = None
    fieldc     = 0


    data = None


    @classmethod
    def set_fields(self, fields):

        if type(fields) == list:
            for f in fields:
                if type(f) != str:
                    print("Error: Field names are incorrect.")
                    return(False)
            self.fieldnames = [ f for f in fields ] 
        elif type(fields) == int:
            self.fieldnames = None
            self.fieldc = fields
        else:
            print("Error: in fields.")
            return(False)

        return(True)
   
# add_data(data)
#                   Will add data to internal running script.

    @classmethod
    def add_data(self, D):
        if self.fieldnames == None:
            c = self.fieldc
        else:
            c = len(self.fieldnames)

        if len(D) != c:
            print("Error: Can not add data.")
            return()

        if self.fieldnames != None:
            if self.data == None:
                self.data = [ {self.fieldnames[x]:D[x] for x in range(c)} ]
            else:
                self.data.append({ self.fieldnames[x]:D[x] for x in range(c) })
        else:
            if self.data == None:
                self.data = [ [ d for d in D ] ]
            else:
                self.data.append([ d for d in D ])

#   fwrite_data(header)
#                           Will write the internally stored data to file.
#                           header = True, write the header for initializing the file.
#                           Else, with header = False or no passed argument, 
#                           then write the data to the file.
   
    @classmethod
    def fwrite_data(self, header = False):
        if self.filename == "":
            return(False)

        print(" X  : : ", self.fieldnames)
        try:
            with open(self.filename, "a", newline="") as dbhf:
    
            #######################
            #
            #   Make sure writing the header only happens if there are field names. Else,
            #   don't write the header.
            #
            #######################
                if header == True:     
                    if self.fieldnames != None:     
                        writer = csv.DictWriter(dbhf, quoting = csv.QUOTE_NONNUMERIC, fieldnames=self.fieldnames)
                        writer.writeheader()
                else:
                    if self.fieldc == 0:
                        writer = csv.DictWriter(dbhf, quoting = csv.QUOTE_NONNUMERIC, fieldnames = self.fieldnames)
                    else:
                        writer = csv.writer(dbhf, quoting = csv.QUOTE_NONNUMERIC)
                    for d in self.data:
                        writer.writerow(d)
                    self.data = None
            return(True)
        except:
            return(False)


################################################################
#
#       fread_data(field data)    Will load data by field data.
#
#       field data =  [ [ field name a, [ dataa1, dataa2,...] ],
#                       [ field name b, [ datab1, datab2,...] ] ... ]
#
#                     [ [ field number a, [ dataa1, dataa2,... ] ],
#                       [ field number b, [ datab1, datab2,... ] ] ... ]
#
#                       Will load all data from field name a with dataa1,
#                       dataa2... and field name b with datab1, datab2,....
#
#                       if COUNT == True, then this routine will not load the data
#                       but will return the count of data.
#
#                       Will auto clear the internal data if COUNT == False
#
#                       c = -1   Error and data wasn't read.
#                       c >= 0   Data was read.
#
################################################################

    @classmethod
    def fread_data(self, fd, COUNT=False):
        
        if self.filename == "":
            return(-1)

        c = 0

        found = False

        if COUNT == False:
            self.data = []

        try:
            with open(self.filename, "r", newline="") as dbhf:
    
                if self.fieldc == 0:
                    reader = csv.DictReader(dbhf, quoting = csv.QUOTE_NONNUMERIC)
                else:
                    reader = csv.reader(dbhf, quoting = csv.QUOTE_NONNUMERIC)
    
                for row in reader:
    
                    if fd == None:                  # Store all data.
                        self.data.append( { f:int(row[f]) for f in row} )
                    else:
                        for f in fd:                # Search field data.
                            found = False
                            if self.fieldc != 0:    # Read field names.
                                for x in range(len(f[1])):
                                    if row[f[0]] == f[1][x]:
                                        found = True
                                        break
                            else:
                            
                                for x in range(len(f[1])):
                                    if row[f[0]] == f[1][x]:
                                        found = True
                                        break
    
                            if found == False:
                                break
    
                        if found == True:
                            if COUNT == True:           # Count data.
                                c+=1 
                            else:
                                if self.fieldc == 0:
                                    self.data.append( {f:int(row[f]) for f in row } ) 
                                else:
                                    self.data.append( [ int(f) for f in row] )       # Add data.

        except:
            return(-1)

        return(c)
                







