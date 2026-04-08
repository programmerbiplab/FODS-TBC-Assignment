'''The following program takes input of ingredients, recipes and
creates a memory storage of all the recipes, the user wants to store
each having a unique number to get it conveniently'''

# Creating a Class for a single Recipe
class Recipe:
    def __init__(self, rid, name, ingredients, description):
        self.id = rid
        self.name = name
        self.ingredients = ingredients
        self.description = description

    def display(self):
        print("\n--- Recipe Details ---")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Ingredients:", self.ingredients)
        print("Description:", self.description)

# Creating a Class for managing a collection of entered Recipes
class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        print(f"Recipe '{recipe.name}' added successfully.")

    def display_all_recipes(self):
        if not self.recipes:
            print("\nNo recipes in the book.")
        else:
            print("\n=== All Recipes ===")
            for recipe in self.recipes:
                recipe.display()


# Main part of program
recipe_book = RecipeBook()

while True:
    print("\n--- Recipe Book Menu ---")
    print("1. Add Recipe")
    print("2. View All Recipes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        rid = input("Enter Recipe ID: ")
        name = input("Enter Recipe Name: ")
        ingredients = input("Enter Ingredients (comma separated): ")
        description = input("Enter Description: ")
        recipe = Recipe(rid, name, ingredients, description)
        recipe_book.add_recipe(recipe)

    elif choice == '2':
        recipe_book.display_all_recipes()

    elif choice == '3':
        print("Exiting Recipe Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

# by Biplab Prasad Gajurel 25024641