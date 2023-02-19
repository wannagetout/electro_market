from item import Item


if __name__ == '__main__':
	item1 = Item('Смартфон', 10000, 20)
	item2 = Item('Ноутбук', 20000, 5)

	print(item1.total_price())
	print(item2.total_price())

	Item.discount = 0.8
	item1.calculate_discount()

	print(item1.total_price())
	print(item2.total_price())

	print(Item.items)
