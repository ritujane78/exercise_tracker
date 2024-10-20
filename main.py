import requests
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

GENDER = "F"
WEIGHT_KG = "51"
HEIGHT_CM = "158"
AGE = "32"

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/37dce00b21cf020eef1a5067503b773c/workoutTracking/workouts"

nutrition_config ={
    "query": input("Enter your workout for today:"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}



headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

response = requests.post(url=nutrition_endpoint,json=nutrition_config, headers=headers)
result = response.json()
# print(result['exercises'])
for each in result['exercises']:
    # print(each["user_input"])
    today = dt.datetime.now()
    formatted_date = today.strftime("%d/%m/%y")
    formatted_time = today.strftime("%H:%M:%S")
    sheety_config = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise":each["user_input"].title(),
            "duration": each["duration_min"],
            "calories": each["nf_calories"]
        }
    }
    # print(sheety_config)
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_config)
    print(sheety_response.text)
    print("Done! Check the workout sheet.")

