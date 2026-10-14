import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['latitude']['longitude']


# Get temperature for diffrent cities
Paris_temp = get_weather(48.86, 2.35)
London_temp = get_weather(51.50, -0.12)
Tokyo_temp = get_weather(35.68, 139.69)


print(f"Paris: {Paris_temp}")
print(f"London: {London_temp}")
print(f"Tokyo: {Tokyo_temp}")