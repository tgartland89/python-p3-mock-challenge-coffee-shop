class Customer:
    def __init__(self, name):
        self.name = name
# add self._orders and ._coffees with empy arrays 
        self._orders = []
        self._coffees = []
        
        
    def orders(self, new_order=None):
        from classes.order import Order

# add the if new_order and isinstance(:) appending new_orders and retuning _orders.   
      
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
            
        return self._orders

    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        
 # add the if new_order and isinstance() and new_coffe not in self._cofees- also dont forget to append and return           
        if new_coffee and isinstance(new_coffee, Coffee) and new_coffee not in self._coffees: 
            
            self._coffees.append(new_coffee)
            
        return  self._coffees
    

# NOTES:

# this code represents a customer. Each customer has a name and can place orders for different coffees. 
# The customer can keep track of their orders and the different types of coffees they have ordered. 
# The orders method allows adding new orders to the customer's list, 
# and the coffees method allows adding new coffee types to the customer's list. 

# the class Customer
# When we create an instance of this class, we pass a name to it, which represents the name of the customer. 
# It also sets two empty lists: _orders to store orders placed by this customer and _coffees to store the coffees the customer has ordered.

#def orders
# takes an optional parameter called new_order. If a new order is provided and it is an instance of the Order class, 
# it adds that order to the _orders list. Finally, it returns the list of orders.

# def coffees
#  It takes an optional parameter called new_coffee. If a new coffee is provided, it checks whether it is an instance of the Coffee class 
# and if it is not already in the _coffees list. 
# If both conditions are true, it adds that coffee to the _coffees list. 
# Finally, it returns the list of coffees



# CODE w/out Notes: 

# class Customer:
#     def __init__(self, name):
#         self.name = name
#         self._orders = []
#         self._coffees = []
        
        
#     def orders(self, new_order=None):
#         from classes.order import Order
#         if new_order and isinstance(new_order, Order):
#             self._orders.append(new_order)
            
#         return self._orders

    
#     def coffees(self, new_coffee=None):
#         from classes.coffee import Coffee        
#         if new_coffee and isinstance(new_coffee, Coffee) and new_coffee not in self._coffees:        
#             self._coffees.append(new_coffee)
            
#         return  self._coffees