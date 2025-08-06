
import os 
import requests
#import webbrowser
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("SPOONACULAR_API_KEY") #the spoonacular api key.

query = input("Enter food ") #the food that we must obtain the recipe for
search_url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&number=1&apiKey={api_key}"
allergies = ["eggs", "milk", "fish", "peanuts", "flour", "sugar"] #allergies, im going to make this user inputed soon
newIngredients = [] # stores the ingredients found in recipe

response = requests.get(search_url) #http request to find recipe for query
data = response.json() #recipe info
print(data) #im going to do more with this soon such as dispalying the image found on the actual spoonacular page
if data["results"]:
    recipe_id = data["results"][0]["id"] #I am going to make it such that you can choose which food recipe you want
    info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}" 

    recipe_info = requests.get(info_url).json()
    print("image URL: ", recipe_info["image"])
    #webbrowser.open(recipe_info["image"])

    print(f"Recipe: {recipe_info['title']}")
    print(" Ingredients:")
    for ingredient in recipe_info["extendedIngredients"]:
        print("-", ingredient["original"])
        for allergy in allergies:
           if allergy.lower() in ingredient["original"].lower():
               print("Allergy: ", ingredient["original"])
               newIngredients.append(ingredient["original"])
else:
    print("No recipes found.")
print(newIngredients)


