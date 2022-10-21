# Google-ICAL-Weather-Integration
Uses a [weather api](https://open-meteo.com/en) to request weather data for the next 7 days and integrates it into Google Calendar [^1]

![image](https://user-images.githubusercontent.com/56944714/197138994-32a56871-bf07-489a-80b9-dbfeca120b71.png)


## How to run
1. Modify the desired configs (See [config](#configuration) section)
1. run `docker compose build` to build the images needed
1. run `docker compose up -d` to start the service
1. use Google's calendar 'import from URL' feature to point Google to the service
1. Profit

## Configuration
The Calendar Service has a [config file](calendar_service/calendar_service/config.hamconf), the file is a custom configuration language I decided to use to test the maturity of the language ([documentation](https://github.com/hamolicious/hamconf)). All of the config variables are commented for easy modification.


[^1]: May work with non "Google" calendars however that has not been tested
