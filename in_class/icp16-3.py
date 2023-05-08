# Iris Canavan, Section 3

import requests
import json
from datetime import datetime, timedelta

response = requests.get("https://api.weather.gov/gridpoints/MTR/84,106/forecast")
response_text = response.text
data = json.loads(response.text)

object_data = datetime.fromisoformat(data["properties"]["periods"][0]["startTime"])

print()
print("Forecast for:", object_data.strftime("%B %d, %Y"))
str_header = ""
for day in range(7):
	forecast_date = object_data + timedelta(days = day)
	str_header += forecast_date.strftime("%D") + "      "
print(str_header)
print("-" * 95)
str_output = ""
for item in data["properties"]["periods"]:
	str_output += str(item["temperature"]) + "     "
print(str_output)
