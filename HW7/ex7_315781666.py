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
	name = None
	price = None
	calories = None
	toppings = []

	def __init__(self, name, price, calories, toppings):
		self.name = name
		if price > 0:
			self.price = price
		else:
			raise ValueError("Price can't be negative")
		if calories > 0:
			self.calories = calories
		else:
			raise ValueError("Calories can't be negative")
		if toppings:
			self.toppings.extend(toppings)
	
	def get_final_price(self, size="Family"):
		if size == "Family":
			return self.price
		if size == "XL":
			return self.price * 1.25
		if size == "Personal":
			return self.price * 0.6
		else:
			raise ValueError("Invalid size")
	
	def add_topping(self, topping, calories, price):
		if topping not in self.toppings:
			self.toppings.extend(topping)
			self.calories += calories
			self.price += price
		else:
			raise ValueError("Topping already exists on the pizza")
	
	def remove_topping(self, topping, calories, price):
		if topping in self.toppings:
			self.toppings.remove(topping)
			self.calories -= calories
			self.price -= price
			if self.price < 0 or self.calories < 0:
				raise ValueError("Calories or Price became negative...")
		else:
			raise ValueError("Topping already exists on the pizza")


#########################################
# Question 3 - do not delete this comment
#########################################


class Meal:
	beverage = None
	pizza = None

	def __init__(self, beverage, pizza):
		self.beverage = beverage
		self.pizza = pizza

	def get_final_price(self, beverage_size, pizza_size):
		return self.beverage.get_final_price(beverage_size) + self.pizza.get_final_price(pizza_size)
	
	def is_healthy(self):
		if self.pizza.calories and self.beverage.is_diet:
			return True
		else:
			return False


# Tests
diet_coke = Beverage("Coca Cola", 15, True)
my_pizza = Pizza("Four Cheese", 50, 1200, ['Mozza', 'Gouda', 'Goat Cheese', 'Parm'])
my_meal = Meal(diet_coke, my_pizza)
pass