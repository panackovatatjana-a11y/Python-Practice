import json
import os

file_path = "data/recipes.json"

# load recipes
def load_recipes():
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

# save recipes
def save_recipes(recipes):
    with open(file_path, "w") as f:
        json.dump(recipes, f)

def add_recipe(recipes):
    print("Add recipe")
    title = input("Title: ")
    ing = input("Ingredients (comma separated): ")
    inst = input("Instructions: ")

    recipe = {
        "title": title,
        "ingredients": [i.strip() for i in ing.split(",")],
        "instructions": inst
    }

    recipes.append(recipe)
    save_recipes(recipes)
    print("Saved.")

def view_recipes(recipes):
    if not recipes:
        print("No recipes.")
        return

    for i, r in enumerate(recipes, 1):
        print("\n", i, r["title"])
        print("Ingredients:", ", ".join(r["ingredients"]))
        print("Instructions:", r["instructions"])

def search_recipes(recipes):
    key = input("Search: ").lower()
    found = []

    for r in recipes:
        if key in r["title"].lower():
            found.append(r)
        else:
            for ing in r["ingredients"]:
                if key in ing.lower():
                    found.append(r)
                    break

    if not found:
        print("Nothing found.")
    else:
        for r in found:
            print("-", r["title"])

def edit_recipe(recipes):
    view_recipes(recipes)
    try:
        num = int(input("Number to edit: ")) - 1
        r = recipes[num]
    except:
        print("Wrong number.")
        return

    new_title = input("New title (leave empty): ")
    new_ing = input("New ingredients (leave empty): ")
    new_inst = input("New instructions (leave empty): ")

    if new_title:
        r["title"] = new_title
    if new_ing:
        r["ingredients"] = [i.strip() for i in new_ing.split(",")]
    if new_inst:
        r["instructions"] = new_inst

    save_recipes(recipes)
    print("Updated.")

def delete_recipe(recipes):
    view_recipes(recipes)
    try:
        num = int(input("Number to delete: ")) - 1
        removed = recipes.pop(num)
        save_recipes(recipes)
        print("Deleted:", removed["title"])
    except:
        print("Wrong number.")

def menu():
    recipes = load_recipes()

    while True:
        print("\n1. Add")
        print("2. View")
        print("3. Search")
        print("4. Edit")
        print("5. Delete")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            view_recipes(recipes)
        elif choice == "3":
            search_recipes(recipes)
        elif choice == "4":
            edit_recipe(recipes)
        elif choice == "5":
            delete_recipe(recipes)
        elif choice == "6":
            break
        else:
            print("Invalid option.")

menu()
