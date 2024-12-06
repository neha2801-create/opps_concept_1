
from item import Item 

class Phone(Item):     # CHILD CLASS with use of SUPER 
    
    
    # Concept Super function 
    all =[]
    
    def __init__(self, name, quantity, price, broken_phones = 0):
        
        # Call to super funtion to have access to all attribites / methods
        super().__init__(
            name, price, quantity
        )
        
        
        # Run validations to received arguments 
        # assert quantity >=0      ----------NOT REQUIRED LINE DUE TO SUPER 
        # assert price >=0         ----------NOT REQUIRED LINE DUE TO SUPER 
        assert broken_phones >= 0 
   
   
        
        # Assign o self object 
        # self.name = name   # passing above passed name to object's name   ----------NOT REQUIRED LINE DUE TO SUPER 
        #                     # this one line replaces                     ----------NOT REQUIRED LINE DUE TO SUPER 
        #                     # item1.name = "Phone" and                    ----------NOT REQUIRED LINE DUE TO SUPER 
        #                     # item2.name = "Pen"                          ----------NOT REQUIRED LINE DUE TO SUPER 

        # self.quantity = quantity    # passing above passed name to object's name  ----------NOT REQUIRED LINE DUE TO SUPER 
        #                               # this one line replaces                    ----------NOT REQUIRED LINE DUE TO SUPER 
        #                               # item1.quantity = 5 and                    ----------NOT REQUIRED LINE DUE TO SUPER 
        #                               # item2.quantity = 2                        ----------NOT REQUIRED LINE DUE TO SUPER 

        # self.price = price    # passing above passed name to object's name         ----------NOT REQUIRED LINE DUE TO SUPER 
        #                         # this one line replaces                          ----------NOT REQUIRED LINE DUE TO SUPER 
        #                         # item1.price = 100 and                            ----------NOT REQUIRED LINE DUE TO SUPER 
        #                         # item2.price = 200                                ----------NOT REQUIRED LINE DUE TO SUPER 
                                
        self.broken_phones = broken_phones  # passing broken_phones we nwe argument to object 
                                            # this broken_phones is SPECIFIC TO PHONE CLASS 
                                            
           
     