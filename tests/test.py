import pytest

from item import Item
from instances.phone import Phone


def test_items_length_check():
	Item.instantiate_from_csv()
	assert (len(Item.items) == 7)


def test_length_check():
	item = Item('Телефон', 10000, 5)
	assert (item.item_name == 'Телефон')
	item.item_name = 'Item name more 10 letters length'
	with pytest.raises(ValueError):
		item.item_name()


def test_integer_check():
	assert (Item.is_integer(7.0) is True)
	assert (Item.is_integer(5.6) is False)


def test_magic_attr():
	item1 = Item('Телефон', 10000, 5)
	assert (item1.__repr__() == 'Телефон', 10000, 5)
	assert (item1.__str__() == 'Телефон')


def test_add_sim_to_phone():
	phone1 = Phone("iPhone 14", 120_000, 5, 2)
	assert (phone1.sim_value == 2)
	with pytest.raises(ValueError):
		phone1.sim_value = -1
		phone1.sim_value()


def test_add_phone_dunder_method():
	phone1 = Phone("iPhone 14", 120_000, 5, 2)
	phone2 = Phone("iPhone 7", 30_000, 8, 1)
	assert (phone1 + phone2 == 13)


def test_add_items_dunder_method():
	item1 = Item('Телефон', 10000, 5)
	item2 = Item('Ноутбук', 60000, 3)
	assert (item1 + item2 == 8)




