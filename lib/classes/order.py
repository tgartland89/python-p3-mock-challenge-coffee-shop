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


# NOTES:

# this code represents an order placed by a customer for a specific coffee. 
# When an order is created, it is associated with the customer, coffee, and price. 
# The order is added to the all list to keep track of all orders. 
# Additionally, the order is added to the respective lists of orders for the coffee and customer. 
# Similarly, the coffee is added to the list of coffees for the customer. 
# This way, the relationships between orders, customers, and coffees are established and tracked.

# the class Order
# all =[] 
# This line creates a class-level variable called all, which is an empty list. 
# This variable is shared among all instances of the Order class..

# the def __init__
# def __init__(self, customer, coffee, price):
    #     self.customer = customer
    #     self.coffee = coffee
    #     self.price = price
    #     Order.all.append(self)
    #     coffee.orders(self)
    #     coffee.customers(customer)
    #     customer.orders(self)
    #     customer.coffees(coffee)

# this is the initializer or constructor of the Order class. 
# It takes three parameters: customer, coffee, and price. 
# It assigns these values to instance variables of the same names (self.customer, self.coffee, self.price).

# Next, it appends the current instance (self) to the class-level list all using Order.all.append(self). 
# This allows keeping track of all orders placed.

# Then, it calls the orders method of the coffee object, passing self as the new order. 
# This adds the current order to the list of orders for that particular coffee.

# Similarly, it calls the customers method of the coffee object, passing customer as the new customer. 
# This adds the customer to the list of customers for that particular coffee.

# Next, it calls the orders method of the customer object, passing self as the new order. 
# This adds the current order to the list of orders for that customer.

# Finally, it calls the coffees method of the customer object, passing coffee as the new coffee. 
# This adds the coffee to the list of coffees for that customer.


# CODE w/out Notes: 

# class Order:


#     all = []

#     def __init__(self, customer, coffee, price):
#         self.customer = customer
#         self.coffee = coffee
#         self.price = price
#         Order.all.append(self)
#         coffee.orders(self)
#         coffee.customers(customer)
#         customer.orders(self)
#         customer.coffees(coffee)