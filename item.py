class Item:
	discount = 0
	items = []

	def __init__(self, item_name, price, amount):
		self.item_name = item_name
		self.price = price
		self.amount = amount
		Item.items.append(self)

	def total_price(self):
		return self.price * self.amount

	def calculate_discount(self):
		return self.price * self.discount
