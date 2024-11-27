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
    return [spicy_food['name'] for spicy_food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [spicy_food for spicy_food in spicy_foods if spicy_food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
   for spicy_food in spicy_foods:
       print (f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {'🌶' * spicy_food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    
    for spicy_food in spicy_foods:
        if cuisine == spicy_food["cuisine"]:
            return dict(name=spicy_food["name"],cuisine= spicy_food["cuisine"], heat_level =spicy_food["heat_level"])

def print_spiciest_foods(spicy_foods):
   for spicy_food in spicy_foods:
       if spicy_food["heat_level"] > 5:
           print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {'🌶' * spicy_food['heat_level']}")



def get_average_heat_level(spicy_foods):
    average_heat_level= list() 
    my_food = len(spicy_foods)
    for spicy_food in spicy_foods:
        average_heat_level.append(spicy_food["heat_level"])
        
    return sum(average_heat_level) / my_food

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
