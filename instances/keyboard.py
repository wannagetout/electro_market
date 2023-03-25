from item import Item


class MixinKeyboard:

	def __init__(self, name, price, count):
		super().__init__(name, price, count)
		self.__language = 'EN'

	@property
	def language(self):
		return self.__language

	def change_lang(self):
		if self.__language == 'EN':
			self.__language = 'RU'
		else:
			self.__language = 'EN'
		return self.__language


class Keyboard(MixinKeyboard, Item):
	pass
