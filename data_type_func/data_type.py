"""
Python Data Types

Built-in Data Types
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

Text Type:	        str
Numeric Types:	    int, float, complex  jk12
Sequence Types:	    list, tuple, range
Mapping Type:	    dict
Set Types:	        set, frozenset
Boolean Type:	    bool
Binary Types:	    bytes, bytearray, memoryview
None Type:	        NoneType


Getting the Data Type
You can get the data type of any object by using the type() function:

x = 5
print(type(x))


Setting the Data Type

Example	                                        Data Type	
x = "Hello World"	                            str	
x = 20	                                        int	
x = 20.5	                                    float	
x = 1j	                                        complex	
x = True	                                    bool	

x = ["apple", "banana", "cherry"]	            list	
x = ("apple", "banana", "cherry")	            tuple	
x = {"name" : "John", "age" : 36}	            dict	
x = {"apple", "banana", "cherry"}	            set	
x = range(6)	                                range	


x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = b"Hello"	                                bytes	
x = bytearray(5)	                            bytearray	
x = memoryview(bytes(5))	                    memoryview	
x = None	                                    NoneType


"""
# we can find any var data type 
x = 5
print(type(x))