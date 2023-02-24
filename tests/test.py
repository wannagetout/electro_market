from item import Item


def test_item_total_price():
	item1 = Item('Смартфон', 10000, 20)
	item2 = Item('Ноутбук', 20000, 5)
	assert (item1.total_price() == 200000)
	assert (item2.total_price() == 100000)


def test_items_price_after_discount():
	item1 = Item('Смартфон', 10000, 20)
	item2 = Item('Ноутбук', 20000, 5)
	Item.discount = 0.8
	item1.calculate_discount()
	assert (item1.total_price() == 160000)
	assert (item2.total_price() == 100000)
