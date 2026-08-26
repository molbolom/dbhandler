

Usage:


	CLIUI.py
		CLIUI	Is the client interface.

		__init__(history_file, history_dir)		Initializes the class
					and sets the history directory and the history file.

					If history file and directory are left blank, then 
					no history file is written or read from.

		write_history()							Write to the history file.
					(Have not figured out how to automate calling this
					on quit()).

		input()									Will wait for user input.

		ynmessage(message)						Will wait for the user to
					input y, yes, or n, no.




	KeyWord.py
		KeyWord 	Is a library for handling keywords and the functions 
			that are linked to the keywords.

					Each KeyWord is set up by a list, with each element
					being a sub keyword of the previous element.
					[ kwa, kwb, kwc ]  
					kwc will only get executed if kwa & kwb preceded kwc.


		set_default(function)					Sets a default function 
					for when a KeyWord doesn't exist.

        set_errortrap(function)                 Sets a function that will
                    send all arguments to a function so the programmer
                    can utilize error handling.
                  
		new(list, function, FLAGS)				Sets the list of keywords
					to the function.

					FLAGS:		NO_ARGS			The function doesn't take
											any arguments.
				
		execute(list)							Searches for the appropriate
					keyword, then executes the function, and passes the
					remaining list items to the function as arguments.

		get(list)								Gets the list item that 
					contains the function for that list item, and returns
					[ key list item, Remainder List of Arguments ]
					(Not really useful for the programmer). 


	Splitter.py
		Splitter	Splits stringis based on delimiters. 

		new_delm(head, tail, flags)				Adds a delimiter to the
					list of delimiters. Sets flags for that element.

					flags = DISCARD_STRING		Do not add string to list.
							DISCARD_DELMS		Do not keep delimiters in string.

		split(string)							Will split a string based
					on the delimiters that were created on program init.


	datahandler.py
		DBHandler								Modifies and writes to
					a database file.

			set_fields(fields)					Set the field names or
					the length of fields that will be used.

					fields = ["this", "that", "those"] DBHandler will
						use the fields named "this", "that", "those".
					fields = 5						   DBHandler will
						add data in 5 columns.

			add_data(list)						Will check and write
					data to temporary internal memory.

			fwrite_data(header)					Will write temporary
					internal data to file and empty the temporary data.

					if header = True, will initialize the file with 
					the header names. This should be called after file
					creation.



			fread_data( A )						Will read data from 
					a csv file based on A criteria.

					if A is empty, then will read all data into the
					temporary internal data.

					A = [ [fieldname, [data] ],
						  [fieldname, [data] ],...]		Will read the
						  file for the fieldnames containing the data
						  specified for the field names.
				
