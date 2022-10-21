FROM python:3.10.8


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ical_service/ ical_service

EXPOSE 3000

CMD [ "python", "ical_service/google_integration.py" ]
