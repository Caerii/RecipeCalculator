# recipes/ingredient.py
from .nutrient import Nutrient

class Ingredient:
    def __init__(self, name, cost_per_unit, unit, quantity, nutrients: Nutrient, store):
        self.name = name
        self.cost_per_unit = cost_per_unit
        self.unit = unit
        self.quantity = quantity
        self.nutrients = nutrients
        self.store = store

    def total_cost(self):
        return self.cost_per_unit * self.quantity

    def __repr__(self):
        return (f"Ingredient(name={self.name}, cost_per_unit={self.cost_per_unit}, unit={self.unit}, quantity={self.quantity}, "
                f"store={self.store}, nutrients={self.nutrients})")

# Define the ingredients
chicken = Ingredient("chicken", 1, "lb", Nutrient(calories=200, protein=20, fat=5, carbohydrates=0, fiber=0, sugar=0, sodium=100, vitamin_a=0, vitamin_c=0, calcium=2, iron=5), "Supermarket A")
pie_crust = Ingredient("pie crust", 2, "pack", Nutrient(calories=400, fat=20, carbohydrates=50, fiber=2, sugar=5, sodium=300, vitamin_a=0, vitamin_c=0, calcium=10, iron=15), "Supermarket B")
carrots = Ingredient("carrots", 1, "lb", Nutrient(calories=50, fiber=4, carbohydrates=12, sugar=6, vitamin_a=100, vitamin_c=10, calcium=4, iron=2), "Supermarket A")
peas = Ingredient("peas", 1, "lb", Nutrient(calories=70, fiber=5, carbohydrates=15, sugar=5, vitamin_a=10, vitamin_c=40, calcium=2, iron=8), "Supermarket A")
potatoes = Ingredient("potatoes", 1, "lb", Nutrient(calories=110, protein=3, fat=0, carbohydrates=26, fiber=2, sugar=1, sodium=0, vitamin_a=0, vitamin_c=45, calcium=2, iron=6), "Supermarket A")
butter = Ingredient("butter", 3, "tbsp", Nutrient(calories=102, fat=11.5, carbohydrates=0, fiber=0, sugar=0, sodium=91, vitamin_a=7, vitamin_c=0, calcium=0, iron=0), "Supermarket B")
flour = Ingredient("flour", 1, "cup", Nutrient(calories=455, protein=13, fat=1.2, carbohydrates=95.4, fiber=3.4, sugar=0.3, sodium=2, vitamin_a=0, vitamin_c=0, calcium=2, iron=37), "Supermarket B")
onion = Ingredient("onion", 0.5, "cup", Nutrient(calories=32, protein=1, fat=0, carbohydrates=7.6, fiber=1.6, sugar=3.4, sodium=3, vitamin_a=0, vitamin_c=7, calcium=2, iron=1), "Supermarket A")
celery = Ingredient("celery", 0.5, "cup", Nutrient(calories=8, protein=0.4, fat=0.1, carbohydrates=1.5, fiber=0.8, sugar=0.7, sodium=40, vitamin_a=4, vitamin_c=2, calcium=1, iron=1), "Supermarket A")
milk = Ingredient("milk", 1, "cup", Nutrient(calories=103, protein=8, fat=2.4, carbohydrates=12, fiber=0, sugar=12, sodium=107, vitamin_a=10, vitamin_c=0, calcium=30, iron=0), "Supermarket B")
salt = Ingredient("salt", 0.5, "tsp", Nutrient(sodium=1160), "Supermarket B")
pepper = Ingredient("pepper", 0.25, "tsp", Nutrient(), "Supermarket B")
# Add additional ingredients similarly...