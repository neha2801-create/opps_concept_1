# creating class 

class Item:
    def calculate_price_total(self, x, y): # self keyword is used here because  BY DEFUALT python passes OBJECT ITSELF AS 1ST ARGUMENT 
                                     # when we call these methods defined inside class 
                                     # WE CAN NEVER DEFINE A FUNCTION WITHOUT ANY ARGUMENT it will throw an ERROR 
                                     # Always 1 positional argument is required to be passed in defintion that is self (for object)
        
        return x * y 
        

# creating an object 

item1 = Item()  # This is creating a constructor of class Item 
# above line is equivalent to item_word = str(4)


# Now we can write some features or attributes of this object item1 of type Item class using dot "."

item1.name = "Phone"
item1.quantity = 5
item1.price = 10
item1.calculate_price_total(item1.quantity,item1.price ) # 1st parameter is always the OBJECT ITSELF ASSIGNED TO self keyword 

print(item1.calculate_price_total(item1.quantity,item1.price))

# Now Check what is the type of each variable defined which all are related to one item1 

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))

# Result of above print statements : 
                                # <class '__main__.Item'> --> Means we created our own datatype of class Item 
                                # <class 'str'>  --> This is already created as OBJECT OF CLASS STRING 
                                # <class 'int'>  --> This is already created as OBJECT OF CLASS INTEGER 
                                # <class 'int'>  --> This is already created as OBJECT OF CLASS INTEGER
                            
# What next ?? Can we have some body or some function added to perform some action over these object variables?

# Yes by defining methods ( a function defined inside a class is called method) 
# So that these some operations are done over these object attributes or variables related to this object 

                                
                                



