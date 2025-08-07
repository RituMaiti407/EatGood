
import os 
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SPOONACULAR_API_KEY") #the spoonacular api key.

st.title("EatSafe: Guide to eating healthy!")
query = st.text_input("Enter food ") #the food that we must obtain the recipe for
number =1 
allergies = ["eggs", "milk", "fish", "peanuts", "flour", "sugar"] #allergies, im going to make this user inputed soon
newIngredients = [] # stores the ingredients found in recipe

if query:
    search_url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&number={number}&apiKey={api_key}"
    response = requests.get(search_url) #http request to find recipe for query
    data = response.json() #recipe info
    #print(data) #im going to do more with this soon such as dispalying the image found on the actual spoonacular page
    if data["results"]:
        recipe_id = data["results"][0]["id"] #I am going to make it such that you can choose which food recipe you want
        info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}" 
        nutrition_url = f"https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget.json?apiKey={api_key}"

        recipe_info = requests.get(info_url).json()
        nutrition_data = requests.get(nutrition_url).json()
        st.image(recipe_info["image"])


        st.write("#### Nutritional Information:")
        st.write(f"**Calories:** {nutrition_data.get('calories', 'N/A')}")
        st.write(f"**Carbohydrates:** {nutrition_data.get('carbs', 'N/A')}")
        st.write(f"**Fat:** {nutrition_data.get('fat', 'N/A')}")
        st.write(f"**Protein:** {nutrition_data.get('protein', 'N/A')}")

        st.write(f"### Recipe: {recipe_info['title']}")
        st.write("#### Ingredients:")
        for ingredient in recipe_info["extendedIngredients"]:
            st.write("-", ingredient["original"])
            for allergy in allergies:
                if allergy.lower() in ingredient["original"].lower():
                    st.write("Allergy: ", ingredient["original"])
                    newIngredients.append(ingredient["original"])
        if recipe_info.get("analyzedInstructions"):
            st.write("#### Cooking Steps:")
            steps = recipe_info["analyzedInstructions"][0]["steps"]
            for step in steps:
                st.write(f"**Step {step['number']}:** {step['step']}")
            else:
                st.write("No step-by-step instructions available.")
    else:
        st.write("No recipes found.")

st.write(newIngredients)
# python3 -m streamlit run Main.py



