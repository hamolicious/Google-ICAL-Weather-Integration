FROM python:3.10.8


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY calendar_service/ calendar_service

CMD [ "python", "calendar_service/" ]
