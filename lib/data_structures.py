from statistics import mean


spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []

    for food in spicy_foods:
        names.append(food['name'])
    return names
pass

def get_spiciest_foods(spicy_foods):
    spiciest = []
    for food in spicy_foods:
        if food.get('heat_level', 0) > 5:
            spiciest.append(food)
    return spiciest
pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food.get('cuisine')
        heat_level = food['heat_level']
        chili_emojis = " 🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {chili_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if str(cuisine) == food['cuisine']:
            return food
    pass

def print_spiciest_foods(spicy_foods):
    spiciest = []
    for food in spicy_foods:
        if food.get('heat_level', 0) > 5:
            heat_level = food['heat_level']
            food['heat_level'] = heat_level * " 🌶️"
            spiciest.append(food)
    return spiciest

    pass

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    average_heat = total_heat / len(spicy_foods)
    return average_heat


def create_spicy_food(spicy_foods, spicy_food):
    
    pass
