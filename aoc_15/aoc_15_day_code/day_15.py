"""Code to solve puzzle for day 15"""
import os

def solve():
    """Solves the day"""
    file_loc = "inputs/day15.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY15':
            print("Invalid input file header: Day15")
            return ''
     
        return input_file.read()
    else:
        print("Day 15 input file does not exist")
        return ''

def create_ingredients(inputs):
    """Creates a dictionary of the ingredients file"""
    ingredients = {}

    for line in inputs:
        ingredient_name = line.split(": ")[0]
        ingrediant_values = line.split(": ")[1].split(", ")

        ingredients[ingredient_name] = {
            'capacity': int(ingrediant_values[0].split()[1]),
            'durability': int(ingrediant_values[1].split()[1]),
            'flavor': int(ingrediant_values[2].split()[1]),
            'texture': int(ingrediant_values[3].split()[1]),
            'calories': int(ingrediant_values[4].split()[1]),
        }

    return ingredients

def calculate_best_score(ingredients, cal_target = 0):
    """Takes a list of ingredients and works out the bext scoring recipe for 100 teaspoons"""
    max_score = 0

    ingredient_names = list(ingredients.keys())

    best_recipe = (0,0,0,0)

    for i in range(100):
        for j in range(100-i):
            for k in range(100-i-j):
                h = 100-i-j-k

                if h == 0:
                    continue

                capacity = max(0, 
                    ingredients[ingredient_names[0]]['capacity'] * i + 
                    ingredients[ingredient_names[1]]['capacity'] * j + 
                    ingredients[ingredient_names[2]]['capacity'] * k + 
                    ingredients[ingredient_names[3]]['capacity'] * h 
                )

                durability = max(0, 
                    ingredients[ingredient_names[0]]['durability'] * i + 
                    ingredients[ingredient_names[1]]['durability'] * j + 
                    ingredients[ingredient_names[2]]['durability'] * k + 
                    ingredients[ingredient_names[3]]['durability'] * h 
                )

                flavor = max(0, 
                    ingredients[ingredient_names[0]]['flavor'] * i + 
                    ingredients[ingredient_names[1]]['flavor'] * j + 
                    ingredients[ingredient_names[2]]['flavor'] * k + 
                    ingredients[ingredient_names[3]]['flavor'] * h 
                )

                texture = max(0, 
                    ingredients[ingredient_names[0]]['texture'] * i + 
                    ingredients[ingredient_names[1]]['texture'] * j + 
                    ingredients[ingredient_names[2]]['texture'] * k + 
                    ingredients[ingredient_names[3]]['texture'] * h 
                )

                calories = max(0, 
                    ingredients[ingredient_names[0]]['calories'] * i + 
                    ingredients[ingredient_names[1]]['calories'] * j + 
                    ingredients[ingredient_names[2]]['calories'] * k + 
                    ingredients[ingredient_names[3]]['calories'] * h 
                )

                score = capacity * durability * flavor * texture

                if cal_target != 0 and calories != cal_target:
                    continue

                if score > max_score:
                    max_score = score
                    best_recipe = ((ingredient_names[0],i), (ingredient_names[1],j), (ingredient_names[2],k), (ingredient_names[3],3))

    return (max_score, best_recipe)

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 15 Puzzle 1 - NO INPUTS")
    else:
        ingredients = create_ingredients(inputs.split('\n'))

        output = calculate_best_score(ingredients)

        print("Day 15 Puzzle 1 Solution - " + str(output[0]))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 15 Puzzle 2 - NO INPUTS")
    else:
        ingredients = create_ingredients(inputs.split('\n'))

        output = calculate_best_score(ingredients, cal_target = 500)

        print("Day 15 Puzzle 2 Solution - " + str(output[0]))
    