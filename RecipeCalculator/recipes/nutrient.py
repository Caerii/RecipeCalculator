# recipes/nutrient.py
class Nutrient:
    def __init__(self, calories=0, protein=0, fat=0, carbohydrates=0, fiber=0, sugar=0, sodium=0, vitamin_a=0, vitamin_c=0, calcium=0, iron=0):
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.fiber = fiber
        self.sugar = sugar
        self.sodium = sodium
        self.vitamin_a = vitamin_a
        self.vitamin_c = vitamin_c
        self.calcium = calcium
        self.iron = iron

    def __repr__(self):
        return (f"Nutrient(calories={self.calories}, protein={self.protein}g, fat={self.fat}g, "
                f"carbohydrates={self.carbohydrates}g, fiber={self.fiber}g, sugar={self.sugar}g, "
                f"sodium={self.sodium}mg, vitamin_a={self.vitamin_a}%, vitamin_c={self.vitamin_c}%, "
                f"calcium={self.calcium}%, iron={self.iron}%)")
