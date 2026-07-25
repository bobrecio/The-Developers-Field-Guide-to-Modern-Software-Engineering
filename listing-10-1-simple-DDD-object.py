class Order: 

    def __init__(self, order_id): 

        self.order_id = order_id 

        self.items = [] 

 

    def add_item(self, product, quantity): 

        # business rules would go here 

        self.items.append((product, quantity)) 

 

    def remove_item(self, product, quantity): 

        # business rules would go here 

        self.items.remove((product, quantity)) 