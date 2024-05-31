# recipes/recipes.py
from .ingredient import Ingredient
from .nutrient import Nutrient

class Recipes:
    def __init__(self):
        self.recipes = {}
        self.servings = {}

    def add_recipe(self, name, ingredients_list, servings):
        self.recipes[name] = ingredients_list
        self.servings[name] = servings

    def get_recipe(self, name):
        return self.recipes.get(name, "Recipe not found")

    def list_recipes(self):
        return list(self.recipes.keys())

    def calculate_total_cost(self, name):
        ingredients = self.recipes.get(name, [])
        total_cost = sum(ingredient.total_cost() for ingredient in ingredients)
        return total_cost

    def cost_per_serving(self, name):
        total_cost = self.calculate_total_cost(name)
        servings = self.servings.get(name, 1)
        return total_cost / servings

    def calculate_total_nutrients(self, name):
        ingredients = self.recipes.get(name, [])
        total_nutrients = Nutrient()
        for ingredient in ingredients:
            total_nutrients.calories += ingredient.nutrients.calories * ingredient.quantity
            total_nutrients.protein += ingredient.nutrients.protein * ingredient.quantity
            total_nutrients.fat += ingredient.nutrients.fat * ingredient.quantity
            total_nutrients.carbohydrates += ingredient.nutrients.carbohydrates * ingredient.quantity
            total_nutrients.fiber += ingredient.nutrients.fiber * ingredient.quantity
            total_nutrients.sugar += ingredient.nutrients.sugar * ingredient.quantity
            total_nutrients.sodium += ingredient.nutrients.sodium * ingredient.quantity
            total_nutrients.vitamin_a += ingredient.nutrients.vitamin_a * ingredient.quantity
            total_nutrients.vitamin_c += ingredient.nutrients.vitamin_c * ingredient.quantity
            total_nutrients.calcium += ingredient.nutrients.calcium * ingredient.quantity
            total_nutrients.iron += ingredient.nutrients.iron * ingredient.quantity
        return total_nutrients

    def calculate_cost_per_nutrient(self, name):
        total_cost = self.calculate_total_cost(name)
        total_nutrients = self.calculate_total_nutrients(name)
        cost_per_nutrient = {
            "calories": total_cost / total_nutrients.calories if total_nutrients.calories else float('inf'),
            "protein": total_cost / total_nutrients.protein if total_nutrients.protein else float('inf'),
            "fat": total_cost / total_nutrients.fat if total_nutrients.fat else float('inf'),
            "carbohydrates": total_cost / total_nutrients.carbohydrates if total_nutrients.carbohydrates else float('inf'),
            "fiber": total_cost / total_nutrients.fiber if total_nutrients.fiber else float('inf'),
            "sugar": total_cost / total_nutrients.sugar if total_nutrients.sugar else float('inf'),
            "sodium": total_cost / total_nutrients.sodium if total_nutrients.sodium else float('inf'),
            "vitamin_a": total_cost / total_nutrients.vitamin_a if total_nutrients.vitamin_a else float('inf'),
            "vitamin_c": total_cost / total_nutrients.vitamin_c if total_nutrients.vitamin_c else float('inf'),
            "calcium": total_cost / total_nutrients.calcium if total_nutrients.calcium else float('inf'),
            "iron": total_cost / total_nutrients.iron if total_nutrients.iron else float('inf')
        }
        return cost_per_nutrient

    def chicken_pot_pie(self):
        ingredients_list = [
            Ingredient("chicken", 5.0, "lb", 1, Nutrient(calories=200, protein=20, fat=5, carbohydrates=0, fiber=0, sugar=0, sodium=100, vitamin_a=0, vitamin_c=0, calcium=2, iron=5), "Supermarket A"),
            Ingredient("pie crust", 2.0, "pack", 2, Nutrient(calories=400, fat=20, carbohydrates=50, fiber=2, sugar=5, sodium=300, vitamin_a=0, vitamin_c=0, calcium=10, iron=15), "Supermarket B"),
            Ingredient("carrots", 1.0, "lb", 1, Nutrient(calories=50, fiber=4, carbohydrates=12, sugar=6, vitamin_a=100, vitamin_c=10, calcium=4, iron=2), "Supermarket A"),
            Ingredient("peas", 1.0, "lb", 1, Nutrient(calories=70, fiber=5, carbohydrates=15, sugar=5, vitamin_a=10, vitamin_c=40, calcium=2, iron=8), "Supermarket A"),
            Ingredient("potatoes", 1.0, "lb", 1, Nutrient(calories=110, protein=3, fat=0, carbohydrates=26, fiber=2, sugar=1, sodium=0, vitamin_a=0, vitamin_c=45, calcium=2, iron=6), "Supermarket A"),
            Ingredient("butter", 3.0, "tbsp", 1, Nutrient(calories=102, fat=11.5, carbohydrates=0, fiber=0, sugar=0, sodium=91, vitamin_a=7, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("flour", 1.0, "cup", 1, Nutrient(calories=455, protein=13, fat=1.2, carbohydrates=95.4, fiber=3.4, sugar=0.3, sodium=2, vitamin_a=0, vitamin_c=0, calcium=2, iron=37), "Supermarket B"),
            Ingredient("onion", 0.5, "cup", 1, Nutrient(calories=32, protein=1, fat=0, carbohydrates=7.6, fiber=1.6, sugar=3.4, sodium=3, vitamin_a=0, vitamin_c=7, calcium=2, iron=1), "Supermarket A"),
            Ingredient("celery", 0.5, "cup", 1, Nutrient(calories=8, protein=0.4, fat=0.1, carbohydrates=1.5, fiber=0.8, sugar=0.7, sodium=40, vitamin_a=4, vitamin_c=2, calcium=1, iron=1), "Supermarket A"),
            Ingredient("milk", 1.0, "cup", 1, Nutrient(calories=103, protein=8, fat=2.4, carbohydrates=12, fiber=0, sugar=12, sodium=107, vitamin_a=10, vitamin_c=0, calcium=30, iron=0), "Supermarket B"),
            Ingredient("salt", 0.5, "tsp", 1, Nutrient(sodium=1160), "Supermarket B"),
            Ingredient("pepper", 0.25, "tsp", 1, Nutrient(), "Supermarket B")
        ]
        servings = 4
        self.add_recipe("Chicken Pot Pie", ingredients_list, servings)

    def steak_mushroom_pie(self):
        ingredients_list = [
            Ingredient("steak", 10.0, "lb", 1, Nutrient(calories=250, protein=25, fat=15, carbohydrates=0, fiber=0, sugar=0, sodium=80, vitamin_a=0, vitamin_c=0, calcium=2, iron=20), "Supermarket A"),
            Ingredient("mushrooms", 3.0, "lb", 1, Nutrient(calories=40, fiber=3, carbohydrates=5, sugar=2, vitamin_a=0, vitamin_c=2, calcium=1, iron=2), "Supermarket B"),
            Ingredient("pie crust", 2.0, "pack", 2, Nutrient(calories=400, fat=20, carbohydrates=50, fiber=2, sugar=5, sodium=300, vitamin_a=0, vitamin_c=0, calcium=10, iron=15), "Supermarket B"),
            Ingredient("onion", 1.0, "cup", 1, Nutrient(calories=64, protein=2, fat=0, carbohydrates=15.2, fiber=3.2, sugar=6.8, sodium=6, vitamin_a=0, vitamin_c=14, calcium=4, iron=2), "Supermarket A"),
            Ingredient("garlic", 1.0, "tbsp", 1, Nutrient(calories=4, protein=0.2, fat=0, carbohydrates=1, fiber=0.1, sugar=0, sodium=1, vitamin_a=0, vitamin_c=2, calcium=0, iron=0), "Supermarket A"),
            Ingredient("beef broth", 4.0, "cup", 1, Nutrient(calories=17, protein=3.2, fat=0.5, carbohydrates=1.7, fiber=0, sugar=0, sodium=860, vitamin_a=0, vitamin_c=0, calcium=0, iron=2), "Supermarket B"),
            Ingredient("butter", 3.0, "tbsp", 1, Nutrient(calories=102, fat=11.5, carbohydrates=0, fiber=0, sugar=0, sodium=91, vitamin_a=7, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("flour", 1.0, "cup", 1, Nutrient(calories=455, protein=13, fat=1.2, carbohydrates=95.4, fiber=3.4, sugar=0.3, sodium=2, vitamin_a=0, vitamin_c=0, calcium=2, iron=37), "Supermarket B"),
            Ingredient("salt", 0.5, "tsp", 1, Nutrient(sodium=1160), "Supermarket B"),
            Ingredient("pepper", 0.25, "tsp", 1, Nutrient(), "Supermarket B"),
            Ingredient("thyme", 1.0, "tsp", 1, Nutrient(), "Supermarket B")
        ]
        servings = 4
        self.add_recipe("Steak Mushroom Pie", ingredients_list, servings)

    def sweet_chili_brussels_sprouts(self):
        ingredients_list = [
            Ingredient("brussels sprouts", 2.0, "lb", 1, Nutrient(calories=60, fiber=5, carbohydrates=12, sugar=3, vitamin_a=15, vitamin_c=100, calcium=6, iron=6), "Supermarket A"),
            Ingredient("olive oil", 0.5, "tbsp", 2, Nutrient(calories=120, fat=14, carbohydrates=0, fiber=0, sugar=0, sodium=0, vitamin_a=0, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("sweet chili sauce", 3.0, "bottle", 0.5, Nutrient(calories=50, sugar=10, carbohydrates=12, sodium=200, vitamin_a=0, vitamin_c=0, calcium=0, iron=0), "Supermarket C")
        ]
        servings = 4
        self.add_recipe("Sweet Chili Brussels Sprouts", ingredients_list, servings)

    def buffalo_chicken_mac_n_cheese(self):
        ingredients_list = [
            Ingredient("chicken", 5.0, "lb", 1, Nutrient(calories=200, protein=20, fat=5, carbohydrates=0, fiber=0, sugar=0, sodium=100, vitamin_a=0, vitamin_c=0, calcium=2, iron=5), "Supermarket A"),
            Ingredient("macaroni", 1.0, "lb", 1, Nutrient(calories=200, protein=7, fat=1, carbohydrates=41, fiber=2, sugar=2, sodium=0, vitamin_a=0, vitamin_c=0, calcium=1, iron=5), "Supermarket B"),
            Ingredient("cheddar cheese", 2.0, "cup", 1, Nutrient(calories=440, protein=28, fat=36, carbohydrates=2, fiber=0, sugar=0, sodium=800, vitamin_a=20, vitamin_c=0, calcium=40, iron=2), "Supermarket B"),
            Ingredient("buffalo sauce", 0.5, "cup", 1, Nutrient(calories=25, fat=0, carbohydrates=6, fiber=0, sugar=0, sodium=1250, vitamin_a=0, vitamin_c=0, calcium=0, iron=0), "Supermarket C"),
            Ingredient("milk", 1.0, "cup", 1, Nutrient(calories=103, protein=8, fat=2.4, carbohydrates=12, fiber=0, sugar=12, sodium=107, vitamin_a=10, vitamin_c=0, calcium=30, iron=0), "Supermarket B"),
            Ingredient("butter", 3.0, "tbsp", 1, Nutrient(calories=102, fat=11.5, carbohydrates=0, fiber=0, sugar=0, sodium=91, vitamin_a=7, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("flour", 1.0, "cup", 1, Nutrient(calories=455, protein=13, fat=1.2, carbohydrates=95.4, fiber=3.4, sugar=0.3, sodium=2, vitamin_a=0, vitamin_c=0, calcium=2, iron=37), "Supermarket B"),
            Ingredient("salt", 0.5, "tsp", 1, Nutrient(sodium=1160), "Supermarket B"),
            Ingredient("pepper", 0.25, "tsp", 1, Nutrient(), "Supermarket B")
        ]
        servings = 4
        self.add_recipe("Buffalo Chicken Mac n Cheese", ingredients_list, servings)

    def poke_bowl(self):
        ingredients_list = [
            Ingredient("sushi-grade tuna", 5.0, "oz", 4, Nutrient(calories=130, protein=28, fat=1, carbohydrates=0, fiber=0, sugar=0, sodium=45, vitamin_a=0, vitamin_c=0, calcium=2, iron=6), "Supermarket D"),
            Ingredient("soy sauce", 0.25, "tbsp", 1, Nutrient(calories=10, protein=1, fat=0, carbohydrates=1, fiber=0, sugar=0, sodium=900, vitamin_a=0, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("sesame oil", 0.5, "tsp", 1, Nutrient(calories=60, fat=7, carbohydrates=0, fiber=0, sugar=0, sodium=0, vitamin_a=0, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("green onions", 0.25, "cup", 1, Nutrient(calories=32, protein=1, fat=0, carbohydrates=7.6, fiber=1.6, sugar=3.4, sodium=3, vitamin_a=0, vitamin_c=7, calcium=2, iron=1), "Supermarket A"),
            Ingredient("seaweed", 0.25, "cup", 1, Nutrient(calories=25, protein=1, fat=0, carbohydrates=6, fiber=1, sugar=0, sodium=20, vitamin_a=10, vitamin_c=20, calcium=5, iron=10), "Supermarket B"),
            Ingredient("edamame", 0.5, "cup", 1, Nutrient(calories=120, protein=11, fat=5, carbohydrates=10, fiber=5, sugar=2, sodium=15, vitamin_a=8, vitamin_c=10, calcium=6, iron=10), "Supermarket B"),
            Ingredient("avocado", 0.5, "each", 1, Nutrient(calories=234, protein=3, fat=21, carbohydrates=12, fiber=10, sugar=1, sodium=10, vitamin_a=8, vitamin_c=20, calcium=2, iron=6), "Supermarket A"),
            Ingredient("rice", 0.5, "cup", 1, Nutrient(calories=205, protein=4, fat=0.4, carbohydrates=45, fiber=0.6, sugar=0, sodium=1, vitamin_a=0, vitamin_c=0, calcium=2, iron=4), "Supermarket B"),
            Ingredient("cucumber", 0.5, "each", 1, Nutrient(calories=45, protein=2, fat=0, carbohydrates=11, fiber=2, sugar=4, sodium=2, vitamin_a=4, vitamin_c=20, calcium=2, iron=4), "Supermarket A"),
            Ingredient("sesame seeds", 0.5, "tbsp", 1, Nutrient(calories=52, protein=1.6, fat=4.5, carbohydrates=2.1, fiber=1.1, sugar=0.1, sodium=1, vitamin_a=0, vitamin_c=0, calcium=9, iron=4), "Supermarket B")
        ]
        servings = 1
        self.add_recipe("Poke Bowl", ingredients_list, servings)


    def pasta_dish(self):
        ingredients_list = [
            Ingredient("shrimp", 15.0, "lb", 1, Nutrient(calories=99, protein=24, fat=0.3, carbohydrates=0, fiber=0, sugar=0, sodium=111, vitamin_a=1, vitamin_c=0, calcium=7, iron=10), "Supermarket D"),
            Ingredient("mushrooms", 3.0, "lb", 1, Nutrient(calories=40, fiber=3, carbohydrates=5, sugar=2, vitamin_a=0, vitamin_c=2, calcium=1, iron=2), "Supermarket B"),
            Ingredient("alfredo sauce", 2.0, "cup", 1, Nutrient(calories=500, protein=10, fat=45, carbohydrates=10, fiber=0, sugar=5, sodium=1400, vitamin_a=10, vitamin_c=0, calcium=25, iron=0), "Supermarket B"),
            Ingredient("spinach", 1.0, "lb", 1, Nutrient(calories=65, protein=8, fat=1, carbohydrates=10, fiber=7, sugar=0, sodium=250, vitamin_a=170, vitamin_c=40, calcium=10, iron=20), "Supermarket A"),
            Ingredient("fettuccini", 1.0, "lb", 1, Nutrient(calories=200, protein=7, fat=1, carbohydrates=41, fiber=2, sugar=2, sodium=0, vitamin_a=0, vitamin_c=0, calcium=1, iron=5), "Supermarket B"),
            Ingredient("chives", 1.0, "tbsp", 1, Nutrient(calories=1, protein=0.1, fat=0, carbohydrates=0.2, fiber=0.1, sugar=0, sodium=0.5, vitamin_a=1, vitamin_c=1, calcium=0.1, iron=0.1), "Supermarket A")
        ]
        servings = 4
        self.add_recipe("Pasta Dish", ingredients_list, servings)

    def salmon_hack(self):
        ingredients_list = [
            Ingredient("salmon", 20.0, "lb", 1, Nutrient(calories=206, protein=22, fat=13, carbohydrates=0, fiber=0, sugar=0, sodium=59, vitamin_a=4, vitamin_c=0, calcium=1, iron=2), "Supermarket D"),
            Ingredient("olive oil", 0.5, "tbsp", 1, Nutrient(calories=120, fat=14, carbohydrates=0, fiber=0, sugar=0, sodium=0, vitamin_a=0, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("lemon", 1.0, "each", 1, Nutrient(calories=17, protein=0.6, fat=0.2, carbohydrates=5.4, fiber=1.6, sugar=1.5, sodium=1, vitamin_a=0, vitamin_c=50, calcium=2, iron=2), "Supermarket A"),
            Ingredient("spices", 0.5, "tsp", 1, Nutrient(), "Supermarket B")
        ]
        servings = 4
        self.add_recipe("Salmon Hack", ingredients_list, servings)

    def cheeseburgers(self):
        ingredients_list = [
            Ingredient("ground beef", 10.0, "lb", 1, Nutrient(calories=250, protein=26, fat=15, carbohydrates=0, fiber=0, sugar=0, sodium=75, vitamin_a=0, vitamin_c=0, calcium=1, iron=15), "Supermarket A"),
            Ingredient("american cheese", 2.0, "slice", 4, Nutrient(calories=60, protein=4, fat=5, carbohydrates=1, fiber=0, sugar=0, sodium=240, vitamin_a=4, vitamin_c=0, calcium=10, iron=0), "Supermarket B"),
            Ingredient("tomato", 1.0, "each", 4, Nutrient(calories=22, protein=1, fat=0.2, carbohydrates=4.8, fiber=1.5, sugar=3.2, sodium=6, vitamin_a=20, vitamin_c=30, calcium=1, iron=2), "Supermarket A"),
            Ingredient("lettuce", 1.0, "head", 1, Nutrient(calories=5, protein=0.5, fat=0.1, carbohydrates=1, fiber=0.5, sugar=0.7, sodium=2, vitamin_a=10, vitamin_c=10, calcium=1, iron=1), "Supermarket A"),
            Ingredient("herbs", 0.5, "tsp", 1, Nutrient(), "Supermarket B"),
            Ingredient("portabella mushrooms", 3.0, "each", 4, Nutrient(calories=22, protein=2.2, fat=0.3, carbohydrates=4.3, fiber=1.1, sugar=2.1, sodium=5, vitamin_a=0, vitamin_c=2, calcium=1, iron=2), "Supermarket A"),
            Ingredient("provolone cheese", 2.0, "slice", 4, Nutrient(calories=70, protein=5, fat=5, carbohydrates=1, fiber=0, sugar=0, sodium=240, vitamin_a=4, vitamin_c=0, calcium=15, iron=0), "Supermarket B"),
            Ingredient("red onion", 1.0, "each", 1, Nutrient(calories=45, protein=1, fat=0, carbohydrates=11, fiber=3, sugar=9, sodium=4, vitamin_a=0, vitamin_c=15, calcium=2, iron=2), "Supermarket A"),
            Ingredient("romaine lettuce", 1.0, "head", 1, Nutrient(calories=8, protein=1, fat=0.1, carbohydrates=2, fiber=1, sugar=1, sodium=2, vitamin_a=20, vitamin_c=15, calcium=1, iron=2), "Supermarket A"),
            Ingredient("balsamic vinegar", 0.5, "cup", 1, Nutrient(calories=108, protein=0, fat=0, carbohydrates=26, fiber=0, sugar=26, sodium=4, vitamin_a=0, vitamin_c=0, calcium=2, iron=4), "Supermarket B"),
            Ingredient("garlic", 1.0, "tbsp", 1, Nutrient(calories=4, protein=0.2, fat=0, carbohydrates=1, fiber=0.1, sugar=0, sodium=1, vitamin_a=0, vitamin_c=2, calcium=0, iron=0), "Supermarket A"),
            Ingredient("olive oil", 0.5, "tbsp", 1, Nutrient(calories=120, fat=14, carbohydrates=0, fiber=0, sugar=0, sodium=0, vitamin_a=0, vitamin_c=0, calcium=0, iron=0), "Supermarket B")
        ]
        servings = 4
        self.add_recipe("Cheeseburgers", ingredients_list, servings)

    def brussel_sprout_dish(self):
        ingredients_list = [
            Ingredient("brussels sprouts", 2.0, "lb", 1, Nutrient(calories=60, fiber=5, carbohydrates=12, sugar=3, vitamin_a=15, vitamin_c=100, calcium=6, iron=6), "Supermarket A"),
            Ingredient("olive oil", 0.5, "tbsp", 1, Nutrient(calories=120, fat=14, carbohydrates=0, fiber=0, sugar=0, sodium=0, vitamin_a=0, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("salt", 0.5, "tsp", 1, Nutrient(sodium=1160), "Supermarket B"),
            Ingredient("pepper", 0.25, "tsp", 1, Nutrient(), "Supermarket B")
        ]
        servings = 4
        self.add_recipe("Brussel Sprout Dish", ingredients_list, servings)

    def daal_dish(self):
        ingredients_list = [
            Ingredient("lentils", 2.0, "cup", 1, Nutrient(calories=230, protein=18, fat=0.8, carbohydrates=40, fiber=15, sugar=2, sodium=4, vitamin_a=0, vitamin_c=6, calcium=4, iron=37), "Supermarket A"),
            Ingredient("onion", 1.0, "cup", 1, Nutrient(calories=64, protein=2, fat=0, carbohydrates=15.2, fiber=3.2, sugar=6.8, sodium=6, vitamin_a=0, vitamin_c=14, calcium=4, iron=2), "Supermarket A"),
            Ingredient("tomato", 1.0, "each", 1, Nutrient(calories=22, protein=1, fat=0.2, carbohydrates=4.8, fiber=1.5, sugar=3.2, sodium=6, vitamin_a=20, vitamin_c=30, calcium=1, iron=2), "Supermarket A"),
            Ingredient("garlic", 1.0, "tbsp", 1, Nutrient(calories=4, protein=0.2, fat=0, carbohydrates=1, fiber=0.1, sugar=0, sodium=1, vitamin_a=0, vitamin_c=2, calcium=0, iron=0), "Supermarket A"),
            Ingredient("ginger", 1.0, "tbsp", 1, Nutrient(calories=4, protein=0.1, fat=0, carbohydrates=1, fiber=0.1, sugar=0, sodium=1, vitamin_a=0, vitamin_c=1, calcium=0, iron=0), "Supermarket A"),
            Ingredient("cumin", 0.5, "tsp", 1, Nutrient(), "Supermarket B"),
            Ingredient("turmeric", 0.5, "tsp", 1, Nutrient(), "Supermarket B"),
            Ingredient("chili powder", 0.5, "tsp", 1, Nutrient(), "Supermarket B"),
            Ingredient("coriander", 0.5, "tsp", 1, Nutrient(), "Supermarket B"),
            Ingredient("salt", 0.5, "tsp", 1, Nutrient(sodium=1160), "Supermarket B"),
            Ingredient("oil", 2.0, "tbsp", 1, Nutrient(calories=120, fat=14, carbohydrates=0, fiber=0, sugar=0, sodium=0, vitamin_a=0, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("cilantro", 1.0, "cup", 1, Nutrient(calories=4, protein=0.3, fat=0.1, carbohydrates=1, fiber=0.6, sugar=0, sodium=1, vitamin_a=54, vitamin_c=14, calcium=1, iron=2), "Supermarket A")
        ]
        servings = 4
        self.add_recipe("Daal Dish", ingredients_list, servings)

    def biryani_with_goat(self):
        ingredients_list = [
            Ingredient("goat meat", 20.0, "lb", 1, Nutrient(calories=143, protein=27, fat=3, carbohydrates=0, fiber=0, sugar=0, sodium=75, vitamin_a=0, vitamin_c=0, calcium=2, iron=25), "Supermarket D"),
            Ingredient("rice", 1.0, "cup", 1, Nutrient(calories=205, protein=4, fat=0.4, carbohydrates=45, fiber=0.6, sugar=0, sodium=1, vitamin_a=0, vitamin_c=0, calcium=2, iron=4), "Supermarket B"),
            Ingredient("yogurt", 1.0, "cup", 1, Nutrient(calories=150, protein=8, fat=8, carbohydrates=11, fiber=0, sugar=11, sodium=120, vitamin_a=5, vitamin_c=0, calcium=30, iron=0), "Supermarket B"),
            Ingredient("onion", 1.0, "cup", 1, Nutrient(calories=64, protein=2, fat=0, carbohydrates=15.2, fiber=3.2, sugar=6.8, sodium=6, vitamin_a=0, vitamin_c=14, calcium=4, iron=2), "Supermarket A"),
            Ingredient("tomato", 1.0, "each", 1, Nutrient(calories=22, protein=1, fat=0.2, carbohydrates=4.8, fiber=1.5, sugar=3.2, sodium=6, vitamin_a=20, vitamin_c=30, calcium=1, iron=2), "Supermarket A"),
            Ingredient("garlic", 1.0, "tbsp", 1, Nutrient(calories=4, protein=0.2, fat=0, carbohydrates=1, fiber=0.1, sugar=0, sodium=1, vitamin_a=0, vitamin_c=2, calcium=0, iron=0), "Supermarket A"),
            Ingredient("ginger", 1.0, "tbsp", 1, Nutrient(calories=4, protein=0.1, fat=0, carbohydrates=1, fiber=0.1, sugar=0, sodium=1, vitamin_a=0, vitamin_c=1, calcium=0, iron=0), "Supermarket A"),
            Ingredient("biryani masala", 2.0, "tbsp", 1, Nutrient(), "Supermarket B"),
            Ingredient("mint", 1.0, "cup", 1, Nutrient(calories=40, protein=3.5, fat=0.6, carbohydrates=9, fiber=7, sugar=0, sodium=2, vitamin_a=22, vitamin_c=120, calcium=20, iron=40), "Supermarket A"),
            Ingredient("cilantro", 1.0, "cup", 1, Nutrient(calories=4, protein=0.3, fat=0.1, carbohydrates=1, fiber=0.6, sugar=0, sodium=1, vitamin_a=54, vitamin_c=14, calcium=1, iron=2), "Supermarket A"),
            Ingredient("ghee", 2.0, "tbsp", 1, Nutrient(calories=112, fat=12.7, carbohydrates=0, fiber=0, sugar=0, sodium=0, vitamin_a=7, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("salt", 0.5, "tsp", 1, Nutrient(sodium=1160), "Supermarket B"),
            Ingredient("spices", 0.5, "tsp", 1, Nutrient(), "Supermarket B")
        ]
        servings = 4
        self.add_recipe("Biryani with Goat", ingredients_list, servings)

    def clam_chowder_can(self):
        ingredients_list = [
            Ingredient("canned clam chowder", 2.0, "can", 1, Nutrient(calories=180, protein=7, fat=8, carbohydrates=20, fiber=1, sugar=2, sodium=890, vitamin_a=10, vitamin_c=2, calcium=10, iron=6), "Supermarket B")
        ]
        servings = 2
        self.add_recipe("Clam Chowder (Can)", ingredients_list, servings)

    def summer_corn_chowder(self):
        ingredients_list = [
            Ingredient("corn", 4.0, "ear", 1, Nutrient(calories=77, protein=3, fat=1, carbohydrates=18.5, fiber=2, sugar=6.4, sodium=15, vitamin_a=9, vitamin_c=10, calcium=1, iron=4), "Supermarket A"),
            Ingredient("potatoes", 1.0, "lb", 1, Nutrient(calories=110, protein=3, fat=0, carbohydrates=26, fiber=2, sugar=1, sodium=0, vitamin_a=0, vitamin_c=45, calcium=2, iron=6), "Supermarket A"),
            Ingredient("onion", 1.0, "cup", 1, Nutrient(calories=64, protein=2, fat=0, carbohydrates=15.2, fiber=3.2, sugar=6.8, sodium=6, vitamin_a=0, vitamin_c=14, calcium=4, iron=2), "Supermarket A"),
            Ingredient("celery", 1.0, "cup", 1, Nutrient(calories=16, protein=0.8, fat=0.2, carbohydrates=3, fiber=1.6, sugar=1.4, sodium=80, vitamin_a=8, vitamin_c=4, calcium=2, iron=2), "Supermarket A"),
            Ingredient("garlic", 1.0, "tbsp", 1, Nutrient(calories=4, protein=0.2, fat=0, carbohydrates=1, fiber=0.1, sugar=0, sodium=1, vitamin_a=0, vitamin_c=2, calcium=0, iron=0), "Supermarket A"),
            Ingredient("chicken broth", 4.0, "cup", 1, Nutrient(calories=17, protein=3.2, fat=0.5, carbohydrates=1.7, fiber=0, sugar=0, sodium=860, vitamin_a=0, vitamin_c=0, calcium=0, iron=2), "Supermarket B"),
            Ingredient("milk", 1.0, "cup", 1, Nutrient(calories=103, protein=8, fat=2.4, carbohydrates=12, fiber=0, sugar=12, sodium=107, vitamin_a=10, vitamin_c=0, calcium=30, iron=0), "Supermarket B"),
            Ingredient("butter", 3.0, "tbsp", 1, Nutrient(calories=102, fat=11.5, carbohydrates=0, fiber=0, sugar=0, sodium=91, vitamin_a=7, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("flour", 1.0, "cup", 1, Nutrient(calories=455, protein=13, fat=1.2, carbohydrates=95.4, fiber=3.4, sugar=0.3, sodium=2, vitamin_a=0, vitamin_c=0, calcium=2, iron=37), "Supermarket B"),
            Ingredient("salt", 0.5, "tsp", 1, Nutrient(sodium=1160), "Supermarket B"),
            Ingredient("pepper", 0.25, "tsp", 1, Nutrient(), "Supermarket B"),
            Ingredient("thyme", 1.0, "tsp", 1, Nutrient(), "Supermarket B")
        ]
        servings = 4
        self.add_recipe("Summer Corn Chowder", ingredients_list, servings)

    def custom_clam_chowder(self):
        ingredients_list = [
            Ingredient("clams", 1.0, "lb", 1, Nutrient(calories=148, protein=25.5, fat=2, carbohydrates=5.1, fiber=0, sugar=0, sodium=1025, vitamin_a=1, vitamin_c=22, calcium=13, iron=155), "Supermarket A"),
            Ingredient("potatoes", 1.0, "lb", 1, Nutrient(calories=110, protein=3, fat=0, carbohydrates=26, fiber=2, sugar=1, sodium=0, vitamin_a=0, vitamin_c=45, calcium=2, iron=6), "Supermarket A"),
            Ingredient("onion", 1.0, "cup", 1, Nutrient(calories=64, protein=2, fat=0, carbohydrates=15.2, fiber=3.2, sugar=6.8, sodium=6, vitamin_a=0, vitamin_c=14, calcium=4, iron=2), "Supermarket A"),
            Ingredient("celery", 1.0, "cup", 1, Nutrient(calories=16, protein=0.8, fat=0.2, carbohydrates=3, fiber=1.6, sugar=1.4, sodium=80, vitamin_a=8, vitamin_c=4, calcium=2, iron=2), "Supermarket A"),
            Ingredient("garlic", 1.0, "tbsp", 1, Nutrient(calories=4, protein=0.2, fat=0, carbohydrates=1, fiber=0.1, sugar=0, sodium=1, vitamin_a=0, vitamin_c=2, calcium=0, iron=0), "Supermarket A"),
            Ingredient("clam juice", 2.0, "cup", 1, Nutrient(calories=35, protein=7, fat=0, carbohydrates=2, fiber=0, sugar=0, sodium=540, vitamin_a=0, vitamin_c=0, calcium=4, iron=20), "Supermarket B"),
            Ingredient("cream", 1.0, "cup", 1, Nutrient(calories=414, protein=3, fat=44, carbohydrates=3, fiber=0, sugar=3, sodium=40, vitamin_a=30, vitamin_c=0, calcium=7, iron=0), "Supermarket B"),
            Ingredient("butter", 3.0, "tbsp", 1, Nutrient(calories=102, fat=11.5, carbohydrates=0, fiber=0, sugar=0, sodium=91, vitamin_a=7, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("flour", 1.0, "cup", 1, Nutrient(calories=455, protein=13, fat=1.2, carbohydrates=95.4, fiber=3.4, sugar=0.3, sodium=2, vitamin_a=0, vitamin_c=0, calcium=2, iron=37), "Supermarket B"),
            Ingredient("salt", 0.5, "tsp", 1, Nutrient(sodium=1160), "Supermarket B"),
            Ingredient("pepper", 0.25, "tsp", 1, Nutrient(), "Supermarket B"),
            Ingredient("thyme", 1.0, "tsp", 1, Nutrient(), "Supermarket B")
        ]
        servings = 4
        self.add_recipe("Custom Clam Chowder", ingredients_list, servings)

    def sunny_side_up_eggs(self):
        ingredients_list = [
            Ingredient("eggs", 6.0, "each", 1, Nutrient(calories=70, protein=6, fat=5, carbohydrates=1, fiber=0, sugar=0, sodium=70, vitamin_a=6, vitamin_c=0, calcium=2, iron=4), "Supermarket A"),
            Ingredient("butter", 3.0, "tbsp", 1, Nutrient(calories=102, fat=11.5, carbohydrates=0, fiber=0, sugar=0, sodium=91, vitamin_a=7, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("salt", 0.5, "tsp", 1, Nutrient(sodium=1160), "Supermarket B"),
            Ingredient("pepper", 0.25, "tsp", 1, Nutrient(), "Supermarket B")
        ]
        servings = 2
        self.add_recipe("Sunny Side Up Eggs", ingredients_list, servings)

    def shrimp_rolls(self):
        ingredients_list = [
            Ingredient("shrimp", 15.0, "lb", 1, Nutrient(calories=99, protein=24, fat=0.3, carbohydrates=0, fiber=0, sugar=0, sodium=111, vitamin_a=1, vitamin_c=0, calcium=7, iron=10), "Supermarket D"),
            Ingredient("mayonnaise", 1.0, "cup", 1, Nutrient(calories=1440, protein=2, fat=160, carbohydrates=0, fiber=0, sugar=0, sodium=800, vitamin_a=2, vitamin_c=0, calcium=0, iron=2), "Supermarket B"),
            Ingredient("lemon juice", 0.5, "cup", 1, Nutrient(calories=30, protein=0.5, fat=0.2, carbohydrates=9.2, fiber=0.4, sugar=2.5, sodium=1, vitamin_a=0, vitamin_c=50, calcium=2, iron=2), "Supermarket A"),
            Ingredient("celery", 1.0, "cup", 1, Nutrient(calories=16, protein=0.8, fat=0.2, carbohydrates=3, fiber=1.6, sugar=1.4, sodium=80, vitamin_a=8, vitamin_c=4, calcium=2, iron=2), "Supermarket A"),
            Ingredient("hot dog buns", 4.0, "each", 1, Nutrient(calories=110, protein=4, fat=2, carbohydrates=20, fiber=1, sugar=3, sodium=190, vitamin_a=0, vitamin_c=0, calcium=6, iron=8), "Supermarket B"),
            Ingredient("butter", 3.0, "tbsp", 1, Nutrient(calories=102, fat=11.5, carbohydrates=0, fiber=0, sugar=0, sodium=91, vitamin_a=7, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("salt", 0.5, "tsp", 1, Nutrient(sodium=1160), "Supermarket B"),
            Ingredient("pepper", 0.25, "tsp", 1, Nutrient(), "Supermarket B")
        ]
        servings = 4
        self.add_recipe("Shrimp Rolls", ingredients_list, servings)

    def lemon_garlic_pepper_pasta(self):
        ingredients_list = [
            Ingredient("pasta", 1.0, "lb", 1, Nutrient(calories=200, protein=7, fat=1, carbohydrates=41, fiber=2, sugar=2, sodium=0, vitamin_a=0, vitamin_c=0, calcium=1, iron=5), "Supermarket B"),
            Ingredient("lemon", 1.0, "each", 1, Nutrient(calories=17, protein=0.6, fat=0.2, carbohydrates=5.4, fiber=1.6, sugar=1.5, sodium=1, vitamin_a=0, vitamin_c=50, calcium=2, iron=2), "Supermarket A"),
            Ingredient("garlic", 1.0, "tbsp", 1, Nutrient(calories=4, protein=0.2, fat=0, carbohydrates=1, fiber=0.1, sugar=0, sodium=1, vitamin_a=0, vitamin_c=2, calcium=0, iron=0), "Supermarket A"),
            Ingredient("pepper", 0.5, "tsp", 1, Nutrient(), "Supermarket B"),
            Ingredient("olive oil", 0.5, "tbsp", 1, Nutrient(calories=120, fat=14, carbohydrates=0, fiber=0, sugar=0, sodium=0, vitamin_a=0, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("parmesan cheese", 0.5, "cup", 1, Nutrient(calories=216, protein=20, fat=14, carbohydrates=4, fiber=0, sugar=0, sodium=712, vitamin_a=8, vitamin_c=0, calcium=67, iron=3), "Supermarket B"),
            Ingredient("salt", 0.5, "tsp", 1, Nutrient(sodium=1160), "Supermarket B")
        ]
        servings = 4
        self.add_recipe("Lemon Garlic Pepper Pasta", ingredients_list, servings)

    def creamy_mushroom_spinach_soup(self):
        ingredients_list = [
            Ingredient("mushrooms", 3.0, "lb", 1, Nutrient(calories=40, fiber=3, carbohydrates=5, sugar=2, vitamin_a=0, vitamin_c=2, calcium=1, iron=2), "Supermarket B"),
            Ingredient("spinach", 1.0, "lb", 1, Nutrient(calories=65, protein=8, fat=1, carbohydrates=10, fiber=7, sugar=0, sodium=250, vitamin_a=170, vitamin_c=40, calcium=10, iron=20), "Supermarket A"),
            Ingredient("onion", 1.0, "cup", 1, Nutrient(calories=64, protein=2, fat=0, carbohydrates=15.2, fiber=3.2, sugar=6.8, sodium=6, vitamin_a=0, vitamin_c=14, calcium=4, iron=2), "Supermarket A"),
            Ingredient("garlic", 1.0, "tbsp", 1, Nutrient(calories=4, protein=0.2, fat=0, carbohydrates=1, fiber=0.1, sugar=0, sodium=1, vitamin_a=0, vitamin_c=2, calcium=0, iron=0), "Supermarket A"),
            Ingredient("chicken broth", 4.0, "cup", 1, Nutrient(calories=17, protein=3.2, fat=0.5, carbohydrates=1.7, fiber=0, sugar=0, sodium=860, vitamin_a=0, vitamin_c=0, calcium=0, iron=2), "Supermarket B"),
            Ingredient("cream", 1.0, "cup", 1, Nutrient(calories=414, protein=3, fat=44, carbohydrates=3, fiber=0, sugar=3, sodium=40, vitamin_a=30, vitamin_c=0, calcium=7, iron=0), "Supermarket B"),
            Ingredient("butter", 3.0, "tbsp", 1, Nutrient(calories=102, fat=11.5, carbohydrates=0, fiber=0, sugar=0, sodium=91, vitamin_a=7, vitamin_c=0, calcium=0, iron=0), "Supermarket B"),
            Ingredient("flour", 1.0, "cup", 1, Nutrient(calories=455, protein=13, fat=1.2, carbohydrates=95.4, fiber=3.4, sugar=0.3, sodium=2, vitamin_a=0, vitamin_c=0, calcium=2, iron=37), "Supermarket B"),
            Ingredient("salt", 0.5, "tsp", 1, Nutrient(sodium=1160), "Supermarket B"),
            Ingredient("pepper", 0.25, "tsp", 1, Nutrient(), "Supermarket B")
        ]
        servings = 4
        self.add_recipe("Creamy Mushroom Spinach Soup", ingredients_list, servings)

    # Add other recipes similarly...
