""" Exercise #7. Python for Engineers."""


#########################################
# Question 1 - do not delete this comment
#########################################


class Beverage:
	name = None
	price = None
	is_diet = None
	
	def __init__(self, name, price, is_diet):
		self.name = name
		if price > 0:
			self.price = price
		else:
			raise ValueError("Prices can't be negative")
		self.is_diet = is_diet

	def get_final_price(self, size="Large"):
		if size == "Large":
			return self.price
		if size == "XL":
			return self.price * 1.25
		if size == "Normal":
			return self.price * 0.75
		else:
			raise ValueError("No such size exists.")


#########################################
# Question 2 - do not delete this comment
#########################################


class Pizza:
	
	def __init__(self, name, price, calories, toppings):
		pass
	
	def get_final_price(self, size):
		pass
	
	def add_topping(self, topping, calories, price):
		pass
	
	def remove_topping(self, topping, calories, price):
		pass


#########################################
# Question 3 - do not delete this comment
#########################################


class Meal:
	
	def __init__(self, beverage, pizza):
		pass
	
	def get_final_price(self, beverage_size, pizza_size):
		pass
	
	def is_healthy(self):
		pass


# Tests
diet_coke = Beverage("Coca Cola", 15, True)
pass