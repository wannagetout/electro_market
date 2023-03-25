import csv


class InstantiateCsvError(Exception):
	pass



class Item:
	discount = 1
	items = []

	def __init__(self, item_name, price, amount):
		self.__item_name = item_name
		self.price = price
		self.amount = amount
		Item.items.append(self)

	def total_price(self):
		return self.price * self.amount

	def calculate_discount(self):
		self.price = int(self.price * self.discount)
		return self.price

	@staticmethod
	def instantiate_from_csv():
		try:
			with open('items.csv', 'r', encoding='windows-1251') as file:
				file = csv.DictReader(file, dialect='excel')
				for row in file:
					Item(item_name=row['name'], price=float(row['price']), amount=int(row['quantity']))
		except FileNotFoundError:
			print('Отсутствует файл item.csv')
		except:
			raise InstantiateCsvError('Файл items.csv повреждён')


	@staticmethod
	def is_integer(value):
		return value.is_integer()

	@property
	def item_name(self):
		if len(self.__item_name) <= 10:
			return self.__item_name
		raise ValueError('Длина наименования товара превышает 10 символов.')

	@item_name.setter
	def item_name(self, value):
		self.__item_name = value

	def __add__(self, other):
		if isinstance(other, Item):
			return self.amount + other.amount

	def __repr__(self):
		return f"{self.__item_name}, {self.price}, {self.amount}"

	def __str__(self):
		return f"{self.__item_name}"
