class Order:

# once I had set up code in the coffee.py and customer.py, I was able to get the additioanl tests to start passing by adding he following: 

# adding all in an empty array passed assed 
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        coffee.orders(self)
       
# adding the coffee.orders(self) clears 3 fails from Coffee: 

# FAILED Coffee in coffee.py test num_orders() - assert 0 == 2
# FAILED Coffee in coffee.py coffee has many orders. - assert 0 == 2
# FAILED Coffee in coffee.py coffee orders are of type Order - IndexError: list index out of range
        coffee.customers(customer)

# adding coffee.customers(customer) clears three more Coffee errors:
# FAILED Coffee in coffee.py coffee has many customers. - assert <classes.customer.Customer object at 0x7fc7cd47af70> in []
# FAILED Coffee in coffee.py coffee has unique list of all the customers that have ordered it. - assert 0 == 2
# FAILED Coffee in coffee.py coffee customers are of type Customer - IndexError: list index out of range

        customer.orders(self)
        customer.coffees(coffee)

# adding the customer.orders and customer.coffees clears the final Customer erorrs: 

# FAILED Customer in customer.py customer has many orders - assert 0 == 2
# FAILED Customer in customer.py customer orders are of type Order - IndexError: list index out of range
# FAILED Customer in customer.py customer has many coffees. - assert <classes.coffee.Coffee object at 0x7f1cec36bbb0> in []
# FAILED Customer in customer.py customer has unique list of all the coffees they have ordered. - assert 0 == 2


