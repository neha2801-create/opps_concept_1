import csv # since we need to read a csv file so this package is required

# Differnce between static method and class methods

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
        
        self.price = self.price * self.pay_rate  # pay_rate can only be accessed through Item. before it 
                                                 # WE CANNOT WRITE self.price = self.price * pay_rate (WITHOUT Item.)
                                                 # any method cannot identify pay_rate inside its scope even if its a class attribute
                                                 # this will overwrite the price attribute of all OBJECTS 
                                                 # BEST PRACTICE IS TO CHANGE ITEM TO self 
                                                 # so that if any object has specific pay_rate it will get modifyied else 
                                                 # by default it uses class attribute
                                                 
    # New concept : Decorators are way to convert simple method into a CLASS METHOD
                   # Using decorators on top pf method are just a way to CHANGE METHOD'S BEHAVIOUR 
                   # Converting that specific method with decorator TELLING PYTHON THAT ITS A CLASS METHOD!
    
    @classmethod
    def instantiate_from_csv(cls): # this method is used to instatiate the object itself 
                                    # so this cannot be called by any object because it ITSELF CREATES OBJECT
                                    
                                    # think HOW WILL THIS METHOD BE USED BUT NOT TO BE USED BY ANY OBJECTS??
                                    # WE NEED TO SAVE THIS METHOD FROM objects to use it !!
                                    # How ?? By making it a class method 
                                    # Yes by making this A CLASS METHOD using a DECORATOR !!
                                    
                                    # Here cls (this name can be anything its just convention to write cls or self 
                                    # for our understanding)
                                    # that is class Item is passed as an argument inside this user defined function
                                    # which is a class method
                                    
        with open('concept_4.csv','r') as f:    # permission is 'r' to only read this csv file 
            my_reader = csv.DictReader(f) # To read content in f as LIST OF DICTIONARIES 
            #print(my_reader)
            # OUTPUT OF THIS PRINT : <csv.DictReader object at 0x104916eb0>
            
            # Then convert this my_reader into list 
            items= list(my_reader)
            #print(items)
            # OUTPUT OF THIS PRINT : [{'name': 'Phone', 'price': '100', 'quantity': '1'},
            # {'name': 'Laptop', 'price': '1000', 'quantity': '3'}, {'name': 'Cable', 'price': '10', 'quantity': '5'}]
            # To make this my_reader output MORE READABLE 
            
            # Suppose you want to see all items in this list of objects , how ??
            # iterate thorough aboev list : items
            
            for item in items:
                # print("printing each object thats the aim of this class method, withotu being using by any object, gives us all objects.")
                # print(item)
    
               # This below lines are used to convert each csv row into each OBJECT , 
               # So its a way to convert csv into OBJECTS 
               # pass aurguments such as name, price and quanity based on csv data recevied 
                Item(
                   name = item.get('name'),
                   price = float(item.get('price')),
                   quantity = int(item.get('quantity'))
                )
 
    # STATIC METHODS : Shud do some work that has some logical coneection to the class Item 
    # Difference between Static and Class method 
    # static methods are similar to general methods which receives self as argument to be passed
    
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point .0 
        # For example: 5.0, 10.0
        # Check if passed num (argument) is a float or not ??
        if isinstance(num, float):
            # Count out the float that are integer 
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
            
    
        
# How to access any CLASS METHOD?
# And HOW TO USE CLASS METHOD?
Item.instantiate_from_csv()


# In order to call all objects with its class names 
print(Item.all) 
        
          
# How to access any STATIC METHOD?
# And HOW TO USE STATIC METHOD?
Item.is_integer(5.6) # This method checks the values passed in Class is passing a specific criteria or not
print("Checking the result of static method")
print(Item.is_integer(5.6))
# Output : False 

