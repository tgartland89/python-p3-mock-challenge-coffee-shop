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
    
