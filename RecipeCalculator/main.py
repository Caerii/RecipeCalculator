# main.py
from recipes.recipes import Recipes

def main():
    my_recipes = Recipes()

    # Add recipes
    my_recipes.chicken_pot_pie()
    my_recipes.steak_mushroom_pie()
    my_recipes.sweet_chili_brussels_sprouts()
    my_recipes.buffalo_chicken_mac_n_cheese()
    my_recipes.poke_bowl()
    my_recipes.pasta_dish()
    my_recipes.salmon_hack()
    my_recipes.cheeseburgers()
    my_recipes.brussel_sprout_dish()
    my_recipes.daal_dish()
    my_recipes.biryani_with_goat()
    my_recipes.clam_chowder_can()
    my_recipes.summer_corn_chowder()
    my_recipes.custom_clam_chowder()
    my_recipes.sunny_side_up_eggs()
    my_recipes.shrimp_rolls()
    my_recipes.lemon_garlic_pepper_pasta()
    my_recipes.creamy_mushroom_spinach_soup()

    # List all recipes
    print("Available Recipes:")
    for recipe in my_recipes.list_recipes():
        print(recipe)

    # Get a specific recipe
    # recipe_name = "Chicken Pot Pie"
    # recipe_name = "Poke Bowl"
    recipe_name = "Creamy Mushroom Spinach Soup"
    print(f"\nIngredients for {recipe_name}:")
    ingredients = my_recipes.get_recipe(recipe_name)
    for ingredient in ingredients:
        print(f"- {ingredient.name} ({ingredient.unit}, {ingredient.quantity}): ${ingredient.cost_per_unit} from {ingredient.store}")
        print(f"  Nutrients: {ingredient.nutrients}")

    # Calculate total cost and cost per serving
    total_cost = my_recipes.calculate_total_cost(recipe_name)
    cost_per_serving = my_recipes.cost_per_serving(recipe_name)
    total_nutrients = my_recipes.calculate_total_nutrients(recipe_name)
    cost_per_nutrient = my_recipes.calculate_cost_per_nutrient(recipe_name)

    print(f"\nTotal cost for {recipe_name}: ${total_cost:.2f}")
    print(f"Cost per serving for {recipe_name}: ${cost_per_serving:.2f}")
    print(f"Total nutrients for {recipe_name}: {total_nutrients}")
    print(f"Cost per unit of each nutrient for {recipe_name}:")
    for nutrient, cost in cost_per_nutrient.items():
        print(f"  {nutrient}: ${cost:.2f} per unit")

if __name__ == "__main__":
    main()