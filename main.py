import requests

# Key acquired from https://openweathermap.org/
# Key is read from a text file called 'api_key.txt'
api_key = open('api_key.txt', 'r').read()
while True:
    location = input("Location: ")
    result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={api_key}")
    if result.json()['cod'] == '404':
        print("Location not found, please try again")
        continue
    break

temp = result.json()['main']['temp']
feels_like = result.json()['main']['feels_like']
temp_min = result.json()['main']['temp_min']
temp_max = result.json()['main']['temp_max']

print(f'Today\'s weather for {location}')
print(f'Temperature: {str(temp)}°C')
print(f'Feels Like: {str(feels_like)}°C')
print(f'Low: {str(temp_min)}°C')
print(f'High: {str(temp_max)}°C')