class Product:
    def __init__(self, product_name, product_qty, unit_price):
        self.product_name = product_name
        self.product_qty = product_qty
        self.unit_price = unit_price

    def calculate_total_price(self):
        # returns total price
        return self.unit_price * self.product_qty


class Order(Product):
    def __init__(self, product_name, product_qty, unit_price, order_no):
        Product.__init__(self, product_name, product_qty, unit_price)
        self.order_no = order_no


class Customer(Order):
    def __init__(self, customer_name, customer_email, product_name, product_qty, unit_price, order_no):
        Order.__init__(self, product_name, product_qty, unit_price, order_no)
        self.customer_name = customer_name
        self.customer_email = customer_email

    def get_details(self):
        # returns -
        print("Order No:", self.order_no)
        print("Customer:", self.customer_name)
        print("Customer Email:", self.customer_email)
        print("Name of the product is", "'", self.product_name, "'")
        print("Product Qty is:", self.product_qty)
        print("Unit price is", self.unit_price)
        print("Order total is", customer.calculate_total_price())


customer = Customer('Sanjay Patel', 'sanjay@dummy.com', 'Pencil', 15, 20, 'SO001')
customer.get_details()
