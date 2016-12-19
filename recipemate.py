#recipemate
class Recipe(object):
	def __init__(self, ingredients, preptime, mealtype, gluten):
		self.ingredients = ingredients
		self.preptime = preptime
		self.mealtype = mealtype
		self.gluten = gluten


risotto = Recipe(['onions', 'bacon', 'parmesan', 'peas', 'vegetable stock', 'risotto rice'], 30, 'dinner', False)
chicken_stirfry = Recipe(['chicken', 'onion', 'cornflour', 'chicken stock', 'sugar snap peas', 'peppers', 'brown sugar', 'soy sauce', 'rice noodles'], 30, 'dinner', False)
breaded_chicken = Recipe(['chicken', 'breadcrumbs', 'crushed chillies', 'salad', 'cheese'], 30, 'dinner', False)
pesto_pasta = Recipe(['pasta, pesto'], 15, 'lunch/dinner', True)

recipe_list = [risotto, chicken_stirfry, breaded_chicken, pesto_pasta]




"""
recipes = {
	'Risotto': ['onions', 'bacon', 'parmesan', 'peas', 'vegetable stock', 'risotto rice'],
	'Chicken stirfry': ['chicken', 'onion', 'cornflour', 'chicken stock', 'sugar snap peas', 'peppers', 'brown sugar', 'soy sauce'],
	'Breaded Chicken and baked potato': 
}
ingredients = []

for i in recipes:
	 for j in recipes[i]:
	 	ingredients.append(j)

print "Welcome to RecipeMate, I can either provide you with a random recipe idea, or you can tell me 
"""
