import requests

# We need coordinets go get weather 
latitude = 48.85  # Paris latitude
longitude = 2.35  # Paris longitude


# Build the API url with out parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"


# Make the requests
response = requests.get(url)
data = response.json()

data["current"]