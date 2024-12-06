
# When to use CLASS METHOD and when to use STATIC METHOD?

# Why we need to define a static method inside though it HAS NO RELATION WITH OBJECTS ??

# Because these are the functions which perform some logic on class Item 

# Here static method is_integer() will be used to check if price is integer or not !!

# So it needs to be defined inside Class itself 

# Then why CLASS METHOD IS REQUIRED?

# to instantiate any new object if required!!!

# This is the major difference between static method and class method 

class Item():
    
    @staticmethod
    def is_integer(num): # 1st parameter is not required to be passed it can be empty 
        """
        
        This should do omething that has relation with class but not something 
        that is unique to each instance.
        """
   
    @classmethod
    def instantiate_from_something(cls): # this 1st parameter sis required to be passed atleast 
        """
        This should also do something that has relationship with class, but usually,
        those re used to manipulate different taructures of data o instantiate objects
        like we did with csv.
        """
