import json

with open('calendar_service/data/weather_code.json', 'r') as f:
	icons = json.load(f)

decoder = {
	'umbrella': '☔',
	'cloud': '☁️',
	'sunny': '☀️',
	'sun_behind_small_cloud': '🌤️',
	'partly_sunny': '⛅',
	'cloud_with_snow': '🌨️',
	'cloud_with_lightning_and_rain': '⛈️',
	'sun_behind_large_cloud': '🌥️',
	'fog': '🌫️',
}

for key in icons:
	icons[key]['icon'] = decoder.get(icons[key]['icon'])

