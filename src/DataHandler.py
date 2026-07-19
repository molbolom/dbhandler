

#   DataHandler contains all the database routines for accessing/writing
#   data to a database.

class DBHandler:
    data = []           # Create an empty list.

    fieldnames = []     # The fieldnames used for reading/writing data
   
    
    # read_data( field list )

    # read_data ['fieldA':[data1, data2, data3], 'fieldB':[data1, data2]]

    # Will search .data for the fields that contain data.


    @classmethod
    def read_data(F):


        for a in self.data:
            for f in F:
                
