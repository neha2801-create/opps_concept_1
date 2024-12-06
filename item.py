import csv
 
class Item:           # PARENT CLASS
    
    pay_rate = 0.8 # This is a class attribute that is pay rate after 30% discout on both items (objects)
    
    all = []
    def __init__(self, name, quantity, price):
        
        # Run validations to received arguments 
        assert quantity >=0
        assert price >=0
     
   
   
        
        # Assign to self object  
        self.__name = name   # passing above passed name to object's name    # self.name = name cannot be done because its already 
                            # this one line replaces                            assigned inside property decorator (method name)
                            # item1.name = "Phone" and                          how to assign name in __init__ also ??
                            # item2.name = "Pen"                                using _ before name 

        self.quantity = quantity    # passing above passed name to object's name
                                      # this one line replaces
                                      # item1.quantity = 5 and
                                      # item2.quantity = 2

        self.__price = price    # passing above passed name to object's name # making price PRIVATE ATTRIBUTE AS WELL TO SHOW hwo its set below 
                                # this one line replaces
                                # item1.price = 100 and
                                # item2.price = 200
                                
                          
        # Actions to execute. 
        # This is used to create a list of all objects created using this class.
        # This should print a list of all objects here it will print a list of item1 and item2
        Item.all.append(self)
        
    # Property decorator for ENCAPSULATION OF object attributes 
    
    @property
    # Property decorator = Read Only Attribute
    def name(self):
        print("You are trying to GET name 1st from here ")
        return self.__name , self.__price  # because its already set up in __init__ 
        
    
    # HOW TO REMOVE RESTRICTION FOR ATTRIBITE _name , a private attribite ??
    # By passing that value INSIDE SETTER SO that user can access this private ATTRIBITE EVEN FROM OUTSIDE
    # Creating setter function to make object attributes to be edited or to pass value to them 
    @name.setter
    def name(self, value, price):
        
        # Concept 7 : Encapsulation , applying to attribute price as well, by setting a rule for price 
        if price < 0 :
            raise Exception("Negative Price doesn't exits!!")
        else:
            print("You are trying to SET price 1st from here ")
            self.__price = price
            
            
        if len(value) > 10 :
            raise Exception("Name is too long")
        else:
            print("You are trying to SET name 1st from here ")
            self.__name = value

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
          
          # IMPLEMENTING CONCEPT OF ENCAPSULATION !!    
          # Now we are trying to create something like OBJECT ATTRIBUTE 
          # In form of METHOD Using @property decorator 
          # this method below : read_only_name() will  ACT AS ONE PROPERTY OF object of Item class
    # @property
    # def read_only_name(self):
    #     return "FIXED NAME"
    
    
    # Concept : Abstraction hiding these methods inside one method send_email
    
    
    def __connect(self,smpt_server): # In order to hide this method from OBJECTS/ INSTANCES we need to make this private
        pass
    
    def __prepare_body(self):        # In order to hide this method from OBJECTS/ INSTANCES we need to make this private
        return f"""
          "Hello someone,
          We have {self.name} {self.quantity} times.
          Regards
    """
        
    def __send(self):                 # In order to hide this method from OBJECTS/ INSTANCES we need to make this private
        pass
            
    def send_email(self):
        self.__connect(4555)
        self.__prepare_body()
        self.__send()
        
        
        