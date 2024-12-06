class Item_A ():
  def calculate_price (self, x, y):
    return x * y

# Creating object 1 from class Item and using class function calculate_price

item1 = Item_A()
item1.name = "Phone"
item1.quantity = 5
item1.price = 100



print(item1.calculate_price(item1.quantity, item1.price))

# Creating object 2 from class Item and using class function calculate_price

item2 = Item_A()
item2.name = "Pen"
item2.quantity = 2
item2.price = 200


print(item2.calculate_price(item2.quantity , item2.price))


########################################################

# Here everytime we need to write all attributes names for each object like quantity or price , so its needs to be defined and written for all
# objects everytime

# Problem : Why not remove this repeated asignment of same attributes with a common function or variable ?

# Solution : __init__() function does this , it assigns a prototype for all objects with single keyword : self !!!!

            # self is used inside __init__() function which represents all objects and
            # __init__() function is used to assign all attributes to all objects since all objects = self

            # so self.attribute1 = attribute1 # this makes it specific to respective object to pass individual values for all object when created
            #    self.attribute2 = attribute2
            #.   self.attribute3 = attribute3
            # so on ..
###########################################################

# now use self and remove all reperated attributes assigned for every object every time like for item1 :

"""
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
"""

##########################################
class Item_B():

  # magic method : __init__(self) :

  def __init__(self): # self is passed which means its used to pass all objects like item1, item2, item3 so on for this class
      print( " I am CREATED ")


# Creating object 1 without any attibute

item1 = Item_B() # self = item1

# Creating object 2 without any attribute

item2 = Item_B() # self = item2


############################################
# See __init__(self) gets called twice because 2 objects are created so __init__(self) is called when we create an object


#. Think how this __init__(self) can be used as said earlier its used to remove the repetation of
# assiging object attributes everytime
# so we can use it to

  # write collection of all attributes for each object in this __init__ function to AVOID REPETATION OF ASSIGNING ATTRIBUTES EVERY TIME

      # Also PYTHON HAS A RULE TO CALL __init__() 1st before all next lines once it gets __init__() function in its way
      # So when object is created , __init__() function will be exceuted 1st inside class Item

#############################################
class Item_C():

  def __init__(self, name):

    self.name = name       # means object's attribute name = name value which will be passed when we create each object
    print(f" I am created by object named as {name}")



# Creating object 1

item1 = Item_C("Phone")

# Creating object 2

item2 = Item_C("Pen")

# Creating object 3

item3 = Item_C("Painting")


##########################################################

class Item_D():

    def __init__(self, name, quantity, price):

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


# Creating object 1

item1 = Item_D("Phone", 5, 100)


# Creating object 2

item2 = Item_D("Pen", 2, 200)

#####################################################
class Item_E():

  def __init__(self, name, quantity, price):

    self.name = name
    self.quantity = quantity
    self.price = price

  def calculate_price(self):
    return self.quantity * self.price


# Creating 1st object

item1 = Item_E("Phone", 5, 100) # Here self = item1
item1.calculate_price()       # Means its = Item.calculate_price(item1) = self.quantity * self.price
                              # Here self.quantity * self.price = 5 * 100 = 500 will be returned
                              # since self.quantity = item1.quantiy and self.price = item1.price thats the use of self
print(item1.calculate_price())

# Creating 2nd object

item2 = Item_E("Pen", 2, 200)  # Here self = item2
item2.calculate_price()      # Means its = Item.calculate_price(item2) = self.quantity * self.price
                             # Here self.quantity * self.price = 2 * 200 = 400 will be returned
                             # since self.quanity = item2.quantity and self.price = item2.price
print(item2.calculate_price())


##################################################
class Item_F():

  def __init__(self, name : str, quantity: int, price: float):
    self.name = name
    self.quantity = quantity
    self.price = price

  def calculate_price(self):
    return self.quantity * self.price

# Creating 1st object
item1 = Item_F("Phone", "5", 100)

print(item1.calculate_price())

