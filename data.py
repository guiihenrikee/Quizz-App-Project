import requests
parameters = {
    "amount": 20,
    "type": "boolean",
    "category": 11
}
request = requests.get("https://opentdb.com/api.php?", params=parameters)
request.raise_for_status()
data = request.json()
question_data = data["results"]

