import pytest

from item import Item


def test_items_length_check():
	Item.instantiate_from_csv()
	assert (len(Item.items) == 5)


def test_length_check():
	item = Item('Телефон', 10000, 5)
	assert (item.item_name == 'Телефон')
	item.item_name = 'Item name more 10 letters length'
	with pytest.raises(ValueError):
		item.item_name()



def test_integer_check():
	assert (Item.is_integer(7.0) == True)
	assert (Item.is_integer(5.6) == False)
