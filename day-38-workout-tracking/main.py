import requests
from datetime import datetime
APP_ID = "c7d42c7f"
API_KEY = "6efbf9ca03e2e45d1a78469fed74704b"
WEIGHT = 80
HEIGHT = 155
AGE = 27

USERNAME = "Umamaheswari"
PASSWORD = "Sheety123(!)"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/f88f46ccce32dc8a386ae09290fb6471/workoutTracking/workouts"

exercise_text = input("Tell me what you did today")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
exercise_response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = exercise_response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_input,
                                   auth=(USERNAME, PASSWORD)
                                   )
    print(sheet_response.text)
