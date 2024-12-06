from item import Item 
# from phone import Phone 

# Item.instantiate_from_csv()

# print(Item.all)


item1 = Item("MyItem", 300, 10)

# Setting an attribute of object item1.
item1.name = "New item"

# Getting an attribute of object item1.
print(item1.name)
# print(item1.__name) # this is private , prevented access outside Item class
# Observe : Here on assinging item1.name = "New item", the value of item1.name get changed from 
#          "MyItem" --> "New item"
#          BUT WE DONT WANT USERS TO CHANGE OBJECT'S ATTRIBUTES EVERYTIME , WHAT IF WE WANT TO RESTRICT THIS CHANGE???

"""
   Solution for above issue : 
                               Make OBJECT ATTRIBUTES --> Read Only !!!
                               Means once attributes values are set they should not get changed evrytime
                               on assignment.
                               
                               We should see error when we try to initialize any attributes again !!
                               
                               Here comes: Encapsulation !!
                               
                               # Jumping back to item.py to make this attributes VALUE CONSTANT 
                               # Using decorators !!

"""

# Since read_only_name(self) method is already created inside class Item so we can use it as property of object here

# print("Printing Object item1 new property item1.read_only_name")
# print(item1.read_only_name)

# Now suppose you TRY TO CHANGE item1.read_only_name this property of object from outside it wont change and throw an error

# item1.read_only_name = "User Set Name"

# Error in above line printed :
#     item1.read_only_name = "User Set Name"
# AttributeError: can't set attribute

