class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders =[]
        self._customers = []

# add self. for _orders & _customers as and set them as empy arrays 
        
    def orders(self, new_order=None):
        from classes.order import Order

# add the if new_order and isinstance (): including self._orders and append to the (new_order)- don;t forget to return self.  
        
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        
        return self._orders
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        
# add if new_custmmer with not in self since this will be a new/non existing person and isisisntance (): also append self and don't forget retrun 
        
        if new_customer not in self._customers and isinstance(new_customer, Customer):
            self._customers.append(new_customer)
        
        return self._customers
    
    
    def num_orders(self):

# add the return len() to get NonType
        return len(self._orders)
    
    
 #  adding for order, total, and return cleared error: clears the average 3.5  

    def average_price(self):
        total = 0
        
        for order in self._orders:
            total += order.price
            
        return total/len(self._orders)


# NOTES:

# this code allows you to create a coffee with a name and keep track of orders and customers associated with that coffee. 
# You can add orders to the coffee, get the list of orders, get the list of customers, and calculate the average price of all the orders.

# the class Coffee
# This code defines a class called "Coffee." When we create an instance of this class, we pass a "name" to it, 
# which represents the name of the coffee. It also sets two empty lists: _
# orders to store orders related to this coffee, and _customers to store customers who have ordered this coffee.

#def orders
# It takes an optional parameter called "new_order." If a new order is provided and it is an instance of the "Order" class, 
# it adds that order to the _orders list. Finally, it returns the list of orders.

# def customers 
# It takes an optional parameter called "new_customer." If a new customer is provided, 
# and that customer is not already in the _customers list, and it is an instance of the "Customer" class, 
# it adds that customer to the _customers list. Finally, it returns the list of customers.

# def num_orders
# simply returns the number of orders in the _orders list by using the len() function.

# def aver_price 
# It calculates the average price of all the orders related to the coffee. 
# It initializes a variable called "total" to zero. 
# Then, it iterates over each order in the _orders list and adds the price of each order to the "total" variable. 
# Finally, it returns the average price by dividing the "total" by the number of orders in the _orders list.

# CODE w/out Notes: 

# class Coffee:
#     def __init__(self, name):
#         self.name = name
#         self._orders =[]
#         self._customers = []
        
#     def orders(self, new_order=None):
#         from classes.order import Order     
#         if new_order and isinstance(new_order, Order):
#             self._orders.append(new_order)
        
#         return self._orders
    
#     def customers(self, new_customer=None):
#         from classes.customer import Customer
#         if new_customer not in self._customers and isinstance(new_customer, Customer):
#             self._customers.append(new_customer)
        
#         return self._customers 
    
#     def num_orders(self):
#         return len(self._orders)
   
#     def average_price(self):
#         total = 0
#         for order in self._orders:
#             total += order.price
            
#         return total/len(self._orders)