from icalendar import Calendar
import json
from day import Day
from time import time
from hamconfig import parse_file
import requests
import base64

PATH = 'calendar_service/'

config = parse_file(f'{PATH}config.hamconf')

reset_time = lambda : time() + config.get('CONFIG.wait_time_secs')
end_time = 0
try:
	while True:
		if time() > end_time:
			calendar = Calendar()
			calendar['X-WR-CALNAME'] = 'Weather'
			calendar['X-WR-TIMEZONE'] = 'UTC'
			calendar['X-WR-CALDESC'] = 'Displays weather for the week'

			with open(f'{PATH}data/test.json', 'r') as f:
				data: dict = json.load(f)

			for i in range(7):
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
	print(e)
