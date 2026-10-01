# What should i eat?
import random

# Dictionaries
foods = {
    "Shakshuka": {
        "mood": "healthy",
        "budget": "£",
    },
    "Salmon Poke Bowl": {
        "mood": "healthy",
        "budget": "££",
    },
    "Chicken or Beef Ramen": {
        "mood": "healthy",
        "budget": "£££",
    },
    "Beef and Black Bean Chilli": {
        "mood": "comfort",
        "budget": "£",
    },
    "Chicken Tikka Masala": {
        "mood": "comfort",
        "budget": "££",
    },
    "Big Roast Dinner": {
        "mood": "comfort",
        "budget": "£££",
    },
    "Cheeseburger and Fries": {
        "mood": "fast food",
        "budget": "£",
    },
    "2 Topping Pizza": {
        "mood": "fast food",
        "budget": "££",
    },
    "Loaded Taco Platter": {
        "mood": "fast food",
        "budget": "£££",
    },
    "Small Sushi Platter": {
        "mood": "fancy",
        "budget": "£",
    },
    "Steak Frites": {
        "mood": "fancy",
        "budget": "££",
    },
    "Steak and Truffle Pasta": {
        "mood": "fancy",
        "budget": "£££",
    }
}
starters = {
    "Veggie Spring Rolls": 7.00,
    "Burrata and Peach Salad": 8.50,
    "Bruschetta": 6.00,
    "Olives": 5.00,
    "Hummus and Pitta Bread": 7.25
}

mains = {
    "Seafood Pasta": 18.00,
    "Chicken Pad Thai": 13.50,
    "Pepperoni Pizza": 18.00,
    "Chicken Jalfrezi": 12.00,
    "Beef Burger": 9.00
}

desserts = {
    "Lemon Cheesecake": 8.00,
    "Vegan Brownie": 6.50,
    "Ice Cream": 3.25,
    "Sticky Toffee Pudding": 6.00,
    "Nutella Pizza": 4.00
}

# Functions


def food_rec():
    print("""\nWhat are you in the mood for?
    Healthy
    Comfort
    Fast food
    Fancy""")
    mood = input("My choice is: ").strip().lower()

    print("""\nWhat's your budget?
    £ - cheap
    ££ - moderate
    £££ - splash out""")
    budget = input("In £ signs: ").strip()

    print("""\nAny dietary requirements?
    None
    Vegetarian
    Vegan
    Gluten-free
    Dairy-free""")
    diet = input("My requirements: ").strip().lower()

    for rec, details in foods.items():
        if details["mood"] == mood and details["budget"] == budget:
            print(f"""\nGiven your mood and budget, tonight you're eating...
            {rec}!""")

    if diet == "vegetarian" or diet == "vegan":
        print("Swap out the protein for mushroom or tofu to make this veggie friendly!")

    if diet == "vegan" or diet == "dairy-free":
        print("Skip the cheese/cream to make this dairy-free!")

    if diet == "gluten-free":
        print("Swap out any wheat-based ingredients with a gluten-free grain!")


def find_food(choice, course):
    for food in course:
        if food.lower() == choice.lower():
            return food

    return


def build_meal():

    print("\nLet's design a 3 course meal! At the end, we'll tell you how much to budget for your meal. ")

    print("\nFirst, let's choose a starter:")
    for starter in starters:
        print(starter)
    starter = input("Choose your starter: ").strip()
    starter = find_food(starter, starters)

    print("\nNow choose a main:")
    for main in mains:
        print(main)
    main = input("Choose your main: ").strip()
    main = find_food(main, mains)

    print("\nAnd finally, choose a dessert: ")
    for dessert in desserts:
        print(dessert)
    dessert = input("Choose your dessert by entering its number: ").strip()
    dessert = find_food(dessert, desserts)

    total = starters[starter] + mains[main] + desserts[dessert]

    print(f"""\nGreat choices! You chose:
    {starter} as your starter,
    {main} for the main course,
    and {dessert} to finish it off!
    Your total is £{total}.""")

    if total <= 20:
        print("Budget: Under £20. Nice going!")

    elif total <= 30:
        print("Budget: Under £30. Not bad for a 3 course meal!")

    else:
        print("Budget: up to £40. Expensive taste I see!")


def random_meal():
    while True:
        meal = [starters, mains, desserts]
        course_name = ["Starter", "Main", "Dessert"]

        for i in range(len(meal)):
            choice = random.choice(list(meal[i].keys()))
            print(f"{course_name[i]}: {choice}")

        again = input("Generate another random meal? yes/no: ").lower()
        if again == "no":
            break

# Main programme


while True:
    print("""WHAT SHOULD I EAT?
    Options:
    1. Find something based on my mood
    2. Build my own meal
    3. Randomly choose""")
    choice = input("Choose an option: ")

    if choice == "1":
        food_rec()
        break

    elif choice == "2":
        build_meal()
        break

    elif choice == "3":
        random_meal()
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Enjoy your meal!")
