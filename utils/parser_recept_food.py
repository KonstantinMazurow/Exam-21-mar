import requests
from data.config import RECEPT_API


def get_random_recept_food():
    response = requests.get(RECEPT_API)
    data = response.json()['meals'][0]
    food_name = data['strMeal']
    recept = data['strInstructions']
    img_food = data['strMealThumb']
    ingredients = []
    for i in range(1, 20):
        if data[f'strIngredient{i}'] != "":
            ingredient = data[f'strMeasure{i}'] + " " + data[f'strIngredient{i}']
            ingredients.append(ingredient)
    recept_random = f'{food_name}\n{img_food}\n{recept}\n'
    for row in ingredients:
        recept_random += f'{row}\n'
    return recept_random
