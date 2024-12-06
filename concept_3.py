

# Class attributes 
# Magic attributes 

# Class attribute ?? # We created all instance attributes in concept2.py where all self.attributes were defined 
#

# Now we need some attribute which BELONGS TO CLASS AND ALL ITS INSTANCES AS WELL

class Item: 
    
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

    def calculate_price (self, x, y):
        return x * y
    
    def apply_discount(self): 
        
        self.price = self.price * Item.pay_rate  # pay_rate can only be accessed through Item. before it 
                                                 # WE CANNOT WRITE self.price = self.price * pay_rate (WITHOUT Item.)
                                                 # any method cannot identify pay_rate inside its scope even if its a class attribute
                                                 # this will overwrite the price attribute of all OBJECTS 
                                                 # BEST PRACTICE IS TO 
   
    def apply_discount_BETTER_PRACTICE(self): 
        
        self.price = self.price * self.pay_rate  # pay_rate can only be accessed through Item. before it 
                                                 # WE CANNOT WRITE self.price = self.price * pay_rate (WITHOUT Item.)
                                                 # any method cannot identify pay_rate inside its scope even if its a class attribute
                                                 # this will overwrite the price attribute of all OBJECTS 
                                                 # BEST PRACTICE IS TO CHANGE ITEM TO self 
                                                 # so that if any object has specific pay_rate it will get modifyied else 
                                                 # by default it uses class attribute
          
    def __repr__(self):
                          # USER FRIENDLY WAY TO REPRESENT ALL OBJECTS LINKED TO THIS CLASS Item
        return f"Item('{self.name}', {self.quantity}, {self.price})"                      

# Print class attribute now 

print("Printing class attribute named pay rate")
print(Item.pay_rate)


# Creating object 1 from class Item and using class function calculate_price

item1 = Item("Phone", 5, 100)

# Now access this CLASS ATTRIBUTE From each object/instance level from each instance i.e here its item1

print("Accessing a Class attribute named pay_rate from object level or instance level : ")
print(item1.pay_rate) # Though item1 has no attribute named pay_rate defined inside __init__() still it gets access to this class attribute


# Another MAGIC ATTRIBUTE to know all attributes related to any class is __dict__ method, used as below :
print("Printing all attributes related to class Item")
print(Item.__dict__)  # Give me all sttributes at class level 

# Print result : Prints all attributes of class defined in __init__() and pay_rate (class attribute)


print("Printing all attributes related to Object item1")
print(item1.__dict__)  # Give me all sttributes at OBJECT level 

# Print result : Prints all attributes of object defined in __init__() ONLY DOESN'T INCLUDE pay_rate attribute in print output

# Now apply discount on item1 using class attribute pay_rate 
print("See how class attribute overwrites price attribute of object item1")
item1.apply_discount()
print(item1.price) # Now this price will be overwriten by a change made due to class attribute pay_rate inside apply_discount()

# Suppose we want to have different type of discount for next item 



# Creating item2 

item2 = Item("Pen", 5, 100)

print("See how class attribute overwrites price attribute of object item2")
item2.pay_rate = 0.7 # Applying specific discount percentage to this object Pen 
item2.apply_discount_BETTER_PRACTICE()
print(item2.price) # Now this price will be overwriten by a change made due to class attribute pay_rate inside apply_discount()


# Printing all items using all keyword

print("Printing all objects related to class Item")
print(Item.all)

# Print result is :
# <__main__.Item object at 0x102576fd0>, <__main__.Item object at 0x102576f70>]

# Printing all names of instances 

# for item in Item.all:
#     print("Prnting object names of class Item")
#     print(item.name)
    
    
# Think is there any better way to print all objects using single method?? Yes there is a magic method : __repr__

    