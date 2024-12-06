

# When we create OPPS applications we need to apply its principles
#

"""
    1) ENCAPSULATION
    2) ABSTRACTION
    3) INHERITANCE
    4) POLYMORPHISM
"""

"""        
            ENCAPSULATION : Restricting DIRECT ACCESS !! TO SOME OF THE ATTRIBUTES IN our program
            
            For example ; Restricting number of letter passed in name attribute of object item1 ( in item.py)
                          Inside setters is an example of ENCAPSULATION !
"""

# Go to item.py 

               
from item import Item

item1 = Item("Encapsulation object", 100, 90)

# Able to set value to 3rd argument that is price = 90 here
# Lets restrict this price attribute by making changes isnside item.py in GETTERS & SETTERS

# New restriction or rule for price : Price should NOT BE -ve !!

# Add this rule inside SETTERS that is def name(self, value):

# Now setting -ve PRICE WHICH is against RULE SET 

# item1 = Item("Encapsulation object", 100, -90)

# printout of above error :
#     assert price >=0
# AssertionError

"""
                 ABSTRACTION : Concept that only shows neccessary attributes
                              HIDES THE UNNESSARY DETIALS FROM USERS WHILE creating new objects from class
                              
                 
"""

item1.send_email()

"""
                  INHERITANCE : Allows to resue code around all classes --> PARENT CLAS & CHILD CLASS concept 

"""

"""
                  POLYMORPHISM : Refers use SINGLE TYPE OF ENTITY TO REPRESENT VARIOUS DIFFERENT TYPE OF ENTITIES 
                                ( Poly : many, morphism : forms)
                                 Exmaple : various pre defined function : len(string_1) function : 
                                 len function knows how to deal various types of datatypes passed to it 
                                 it can count, characters in a string, number of elements in a list 

"""

print(" len function used to count number of characters in word : I am learning, with great spirit!!")
print(len(" len function used to count number of characters in  this sentence, I am learning, with great spirit!!"))

print(" len function is also used to count number of elements in a list")
print(len({"len", "function", "is", "also", "used", "to", "count", "number", "of", "elements", "in", "this", "list", "great"}))