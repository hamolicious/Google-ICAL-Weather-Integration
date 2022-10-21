import requests
from datetime import datetime, timedelta

url = 'https://api.open-meteo.com/v1/forecast?latitude=52.6101&longitude=0.2577&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum,snowfall_sum,windspeed_10m_max&timezone=auto&timeformat=unixtime&start_date={start_date}&end_date={end_date}'

def get_todays_date() -> datetime:
	return datetime.now()

def get_weather() -> dict:
	yyyymmdd = lambda dt: dt.strftime('%Y-%m-%d')

	new_url = url.format(
		start_date=yyyymmdd(get_todays_date()),
		end_date=yyyymmdd(get_todays_date() + timedelta(days=7)),
	)

	with requests.get(new_url) as r:
		if r.status_code == 200:
			return r.json()







