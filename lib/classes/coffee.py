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



