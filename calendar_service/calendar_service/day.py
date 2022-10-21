from __future__ import annotations
from icalendar import Event
from datetime import datetime
from hashlib import md5
from hamconfig import parse_file

config = parse_file('calendar_service/config.hamconf')

class Day:
	def __init__(self, data: dict, index: int) -> None:
		self.__event = Event()
		self.desc = ''

		daily_data = data.get('daily')

		get = lambda key : daily_data.get(key)[index]
		hms = lambda time: datetime.fromtimestamp(time).strftime('%H:%M:%S')
		iso8601 = lambda time : time.isoformat().split('T')[0].replace('-', '')

		time = datetime.fromtimestamp(get('time'))

		weather_code = get('weathercode')
		precipitation_sum = get('precipitation_sum')
		precipitation_snow_sum = get('snowfall_sum')

		desc, icon_name = config.get(f'WEATHERCODES.weather_code_{weather_code}')
		icon = config.get(f'ICONS.{icon_name}')

		uid = md5((iso8601(time) + 'hamolicious').encode('UTF-8')).hexdigest()

		maximum_temperature = get('temperature_2m_max')
		minimum_temperature = get('temperature_2m_min')
		sunrise = hms(get('sunrise'))
		sunset = hms(get('sunset'))
		maximum_wind_speeds = get('windspeed_10m_max')

		description = [
			f'Maximum Temperature: {maximum_temperature}°C',
			f'Minimum Temperature: {minimum_temperature}°C',
			f'Sunrise: {sunrise}', # sunrise
			f'Sunset: {sunset}', # sunset
			f'Precipitation: {precipitation_sum}mm', # precipitation
			f'Maximum wind speeds: {maximum_wind_speeds}km/h', # max_windspeed
		]

		self.__event['dtstart'] = iso8601(time)
		self.__event['summary'] = f'{icon} Weather | {desc}'
		self.__event['uid'] = uid
		self.__event['description'] = '\n'.join(description)

	def get_event(self) -> Event:
		return self.__event
