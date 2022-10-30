from __future__ import annotations
from icalendar import Event
from datetime import datetime
from icons import icons
from random import choice
from hashlib import md5
from datetime import datetime


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

		icon = icons.get(str(weather_code)).get('icon')
		desc = icons.get(str(weather_code)).get('desc')

		maximum_temperature = get('temperature_2m_max')
		minimum_temperature = get('temperature_2m_min')
		sunrise = hms(get('sunrise'))
		sunset = hms(get('sunset'))
		maximum_wind_speeds = get('windspeed_10m_max')

		update_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

		description = [
			f'Maximum Temperature: {maximum_temperature}°C',
			f'Minimum Temperature: {minimum_temperature}°C',
			f'Sunrise: {sunrise}',
			f'Sunset: {sunset}',
			f'Precipitation: {precipitation_sum}mm',
			f'Maximum wind speeds: {maximum_wind_speeds}km/h',
			f'Last Update: {update_time}',
		]

		self.__event['dtstart'] = iso8601(time)
		self.__event['summary'] = f'{icon} Weather | {desc}'
		self.__event['uid'] = md5(iso8601(time).encode('UTF-8')).hexdigest()
		self.__event['description'] = '\n'.join(description)

	def get_event(self) -> Event:
		return self.__event
