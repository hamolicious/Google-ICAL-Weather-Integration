from weather import get_weather
from icalendar import Calendar
import json
from day import Day
from time import time
from hamconfig import parse_file
import requests
import base64
import os

PATH = 'calendar_service/'

config = parse_file(f'{PATH}config.hamconf')

reset_time = lambda : time() + config.get('CONFIG.wait_time_secs')
end_time = 0
try:
	while True:
		if time() > end_time:
			calendar = Calendar()
			calendar['X-WR-CALNAME'] = 'Weather'
			calendar['X-WR-TIMEZONE'] = os.environ.get('TZ')
			calendar['X-WR-CALDESC'] = 'Displays weather for the week'

			data: dict = get_weather()

			for i in range(config.get('CONFIG.look_forward_amount')):
				day = Day(data, i)
				calendar.add_component(day.get_event())

			string = calendar.to_ical().decode("utf-8").strip()

			with open(f'{PATH}data/output.ics', 'w') as f:
				f.write(string)

			to_send = base64.b64encode(bytes(string, 'UTF-8'))
			with requests.post('http://ical:3000/update_data', data=to_send) as r:
				print(f'Sending data {r.status_code}')

			end_time = reset_time()
except KeyboardInterrupt:
	quit()
except Exception as e:
	raise e
