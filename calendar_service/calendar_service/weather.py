import requests
from datetime import datetime, timedelta

url = 'https://api.open-meteo.com/v1/forecast?latitude=52.6101&longitude=0.2577&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum,snowfall_sum,windspeed_10m_max&timezone=auto&timeformat=unixtime'

def get_weather() -> dict:
	with requests.get(url) as r:
		if r.status_code == 200:
			return r.json()







