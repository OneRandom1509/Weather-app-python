import requests
while True:

	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

	def getweather(city):
		result = requests.get(url.format(city, api_key))
		
		if result:
			json = result.json()
			city = json['name']
			country = json['sys']['country']
			temp_kelvin = json['main']['temp']
			temp_celsius = temp_kelvin-273.15
			temp_celsius = str(round(temp_celsius, 2)) + ' Degrees Celsius'
			weather1 = json['weather'][0]['main']
			desc = json['weather'][0]['description'].capitalize()
			wind = json['wind']['speed']
			wind_dir = json['wind']['deg']
			humidity = json['main']['humidity']
			final = [city, country, temp_celsius, weather1, desc, wind, wind_dir, humidity]
			return final
		else:
			print("Please enter a real city's name... not an imaginary ones' xd")

	def search(city_name):
		weather = getweather(city_name)
		if weather:
			print(f"{'-'*35}\nCity: {weather[0]}, {weather[1]}\nTemperature: {weather[2]}\nWeather conditions: {weather[3]}\nDescription: {weather[4]}\n\nAdditional Details:\n\tWind speed: {weather[5]}km/h\n\tWind direction: {weather[6]} Degrees\n\tHumidity: {weather[7]}%\n{'-'*35}")
		else:
			return 'Error', f"Cannot find {city}",'\n'+"Please enter a real city's name... not an imaginary ones' xd"

	city = input(">>> Enter the city's name\n>>> ")
	search(city)