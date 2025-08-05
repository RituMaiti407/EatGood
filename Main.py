
import os 
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SPOONACULAR_API_KEY")

query = input("Enter food ")
search_url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&number=1&apiKey={api_key}"

response = requests.get(search_url)
data = response.json()
print(data)
if data["results"]:
    recipe_id = data["results"][0]["id"]
    info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}"

    recipe_info = requests.get(info_url).json()
    print(f"Recipe: {recipe_info['title']}")
    print(" Ingredients:")
    for ingredient in recipe_info["extendedIngredients"]:
        print("-", ingredient["original"])
else:
    print("No recipes found.")
