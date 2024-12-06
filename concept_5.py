# Inheritance could help us to write more than 1 class 

# How to use super() ?

import csv
 
class Item:           # PARENT CLASS
    
    pay_rate = 0.8 # This is a class attribute that is pay rate after 30% discout on both items (objects)
    
    all = []
    def __init__(self, name, quantity, price):
        
        # Run validations to received arguments 
        assert quantity >=0
        assert price >=0
     
   
   
        
        # Assign o self object 
        self.name = name   # passing above passed name to object's name
                            # this one line replaces
                            # item1.name = "Phone" and
                            # item2.name = "Pen"

        self.quantity = quantity    # passing above passed name to object's name
                                      # this one line replaces
                                      # item1.quantity = 5 and
                                      # item2.quantity = 2

        self.price = price    # passing above passed name to object's name
                                # this one line replaces
                                # item1.price = 100 and
                                # item2.price = 200
                                
                          
        # Actions to execute. 
        # This is used to create a list of all objects created using this class.
        # This should print a list of all objects here it will print a list of item1 and item2
        Item.all.append(self)

    def calculate_price (self):
        return self.quantity * self.price
    
    def apply_discount(self): 
        
        self.price = self.price * Item.pay_rate  # pay_rate can only be accessed through Item. before it 
                                                 # WE CANNOT WRITE self.price = self.price * pay_rate (WITHOUT Item.)
                                                 # any method cannot identify pay_rate inside its scope even if its a class attribute
                                                 # this will overwrite the price attribute of all OBJECTS 
                                                 # BEST PRACTICE IS TO 
   
    def __repr__(self):
                          # USER FRIENDLY WAY TO REPRESENT ALL OBJECTS LINKED TO THIS CLASS Item
        # return f"Item('{self.name}', {self.quantity}, {self.price})"      
        return f"{self.__class__.__name__}('{self.name}', {self.quantity}, {self.price})"    
        # above __class__ and __name__ are used to nake this generic to CHild class or parent class, whose ever object is created 
    
class Phone(Item):     # CHILD CLASS
    
    
    # Concept Super function 
    # all = []  # since its inherited from main class Item 
    
    def __init__(self, name, quantity, price, broken_phones = 0):
        
        # Run validations to received arguments 
        assert quantity >=0
        assert price >=0
        assert broken_phones >= 0 
   
   
        
        # Assign o self object 
        self.name = name   # passing above passed name to object's name
                            # this one line replaces
                            # item1.name = "Phone" and
                            # item2.name = "Pen"

        self.quantity = quantity    # passing above passed name to object's name
                                      # this one line replaces
                                      # item1.quantity = 5 and
                                      # item2.quantity = 2

        self.price = price    # passing above passed name to object's name
                                # this one line replaces
                                # item1.price = 100 and
                                # item2.price = 200
                                
        self.broken_phones = broken_phones  # passing broken_phones we nwe argument to object 
                                            # this broken_phones is SPECIFIC TO PHONE CLASS 
                                            
           
        # Actions to execute. 
        # This is used to create a list of all objects created using this class.
        # This should print a list of all objects here it will print a list of item1 and item2
        # Phone.all.append(self) since its inherited from Item class


# Now see how many lines get removed on using SUPER KEYWORD FOR ABOVE METHOD , BELOW METHOD IS ALSO SAME
# onLY DIFFERNEC IS repeated lines from PARENT CLASS Item gets removed on using  SUPER KEYWORD 

class Phone_With_Super(Item):     # CHILD CLASS with use of SUPER 
    
    
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
                                            
           
        # Actions to execute. 
        # This is used to create a list of all objects created using this class.
        # This should print a list of all objects here it will print a list of item1 and item2
        Phone.all.append(self)

    
    # phone1 is created from class Phone which is inherited from parent class Item 
    
phone1 = (Phone("Phone1", 100, 5, 1)) # Phone class which has new attribute broken_phones which is passed here

# phone1 can use all object methods inside parent class
print(phone1.calculate_price())


phone2 = (Phone("Phone2", 200, 15, 2))


# Now check what objects are related to PARENT AND CHILD CLASSES??

print("Prining all objects related to PARENT CLASS AND CHILD CLASS")
print(Item.all)
print(Phone.all)

# Print result : 
# Prining all objects related to PARENT CLASS AND CHILD CLASS
# []
# [Item('Phone1', 100, 5), Item('Phone2', 200, 15)]
# Observe still Phone class has Item in its output for representing its object because we never used __repr__ method in Phone class

# for that we have __class__ and __name__ used inside __repr__ to show Class name of objects specifically in each case, 
# that means __repr__ output willl change as per cCHILD CLASS NAME OR PARENT CLASS NAME

# So make changes in __repr__ of main class Item 



