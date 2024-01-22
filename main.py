import requests

# Key acquired from https://openweathermap.org/
# Key is read from a text file called 'api_key.txt'
api_key = open('api_key.txt', 'r').read()
location = input("Location: ")

result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={api_key}")

temp = result.json()['main']['temp']
feels_like = result.json()['main']['feels_like']
temp_min = result.json()['main']['temp_min']
temp_max = result.json()['main']['temp_max']


print(temp)
print(feels_like)
print(temp_min)
print(temp_max)