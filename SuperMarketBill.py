class Supermarket:
    def __init__(self):
        self.items = []
        self.total_amount = 0.0
        self.discount = 0.0
        self.final_amount = 0.0

    def add_item(self, name, price, quantity):
        item = {
            'name': name,
            'price': price,
            'quantity': quantity,
            'total': price * quantity
        }
        self.items.append(item)
        self.total_amount += item['total']

    def apply_discount(self, discount_percent):
        self.discount = (discount_percent / 100) * self.total_amount
        self.final_amount = self.total_amount - self.discount

    def generate_bill(self):
        bill = "\n--- Supermarket Bill ---\n"
        bill += "{:<20} {:<10} {:<10} {:<10}\n".format('Item', 'Price', 'Quantity', 'Total')
        bill += "-" * 60 + "\n"
        for item in self.items:
            bill += "{:<20} {:<10.2f} {:<10} {:<10.2f}\n".format(item['name'], item['price'], item['quantity'], item['total'])
        bill += "-" * 60 + "\n"
        bill += "{:<40} {:<10.2f}\n".format('Total Amount', self.total_amount)
        bill += "{:<40} {:<10.2f}\n".format('Discount', self.discount)
        bill += "{:<40} {:<10.2f}\n".format('Final Amount', self.final_amount)
        bill += "-" * 60 + "\n"
        print(bill)

# Example usage
supermarket = Supermarket()
supermarket.add_item('Apple', 0.5, 10)
supermarket.add_item('Banana', 0.3, 15)
supermarket.add_item('Milk', 1.2, 2)
supermarket.add_item('Bread', 2.0, 1)
supermarket.apply_discount(10)  # 10% discount
supermarket.generate_bill()
