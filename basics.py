
# Understand why we need OPPS or class creation ??

# Example 1

item1 = "Phone"
item1_price = 500
item1_quantity = 5 
item1_price_total = item1_price * item1_quantity

# Observation : Here we have item1 prefix COMMON to all variables means these variables are related to one OBJECT
               # , so can we do something to create a common collection 
               # Or something some data type which will define this entire item1 at once???
            

# Check what is the type of each variable defined which all are related to one item1 

print(type(item1))
print(type(item1_price))
print(type(item1_quantity))
print(type(item1_price_total))

# Above print results are : 

# We get respectively : 
        # <class 'str'> --> Means : datatype of item1 is AN INSTANCE OF CLASS STRING 
        # <class 'int'> --> Means : datatype of item1_price is AN INSTANCE OF CLASS INTEGER
        # <class 'int'> --> Means : datatype of item1_quantity is AN INSTANCE OF CLASS INTEGER 
        # <class 'int'> --> Means : datatype of item1_price_toal is AN INSTANCE OF CLASS INTEGER
        
# What if we combine all these variables under ONE DATATYPE / OBJECT TYPE Or we can say 
# SINGLE OBJECT with one CLASS containing all these VARIABLES OR ATTRIBUTES 

# Reason : Think what if we want to reuse this OBJECT TYPE again and again ??
#          Then we dont have to create these seperate 4 variables or attributes and  
#          these variables can be combined under one ONJECT TYPE item1
