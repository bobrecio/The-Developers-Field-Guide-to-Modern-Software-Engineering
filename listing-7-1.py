class TestClass: 

    def __init__(self): 

        print("I am the constructor") 

 

    @classmethod 

    def class_level_function(cls): 

        print("I am class level") 

 

    def object_level_function(self): 

        print("I am object level") 

 

# Usage: 

TestClass is not instantiated as an object 

TestClass.class_level_function() # Calls class level function 

 

obj = TestClass()                # Calls constructor 

obj.object_level_function()    # Calls object level function 