import requests
from datetime import datetime, timedelta
from hamconfig import parse_file

url = 'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum,snowfall_sum,windspeed_10m_max&timezone=auto&timeformat=unixtime&start_date={start_date}&end_date={end_date}'

def get_todays_date() -> datetime:
	return datetime.now()

def get_weather() -> dict:
	yyyymmdd = lambda dt: dt.strftime('%Y-%m-%d')

	config = parse_file('calendar_service/config.hamconf')

	new_url = url.format(
		lat=config.get('LOCALE.lat'),
		long=config.get('LOCALE.long'),
		start_date=yyyymmdd(get_todays_date()),
		end_date=yyyymmdd(get_todays_date() + timedelta(days=config.get('CONFIG.look_forward_amount'))),
	)

	with requests.get(new_url) as r:
		if r.status_code == 200:
			return r.json()







