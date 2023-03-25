from item import Item


class Phone(Item):

	def __init__(self, item_name, price, amount, sim: int):
		super().__init__(item_name, price, amount)
		self.__sim = sim

	@property
	def sim_value(self):
		return self.__sim

	@sim_value.setter
	def sim_value(self, value: int) -> None:
		if value > 0:
			if type(value) is int:
				self.__sim = value
		else:
			raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

	def __add__(self, other):
		if isinstance(other, Phone):
			return self.amount + other.amount

	def __repr__(self):
		return f"Phone('{self.item_name}', {self.price}, {self.amount}, {self.__sim})"
