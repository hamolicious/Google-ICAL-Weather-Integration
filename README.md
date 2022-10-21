# Google-ICAL-Weather-Integration
Uses a [weather api](https://open-meteo.com/en) to request weather data for the next 7 days and integrates it into Google Calendar [^1]

![image](https://user-images.githubusercontent.com/56944714/197138994-32a56871-bf07-489a-80b9-dbfeca120b71.png)


## How to run


## Configuration
The Calendar Service has a [config file](calendar_service/calendar_service/config.hamconf):

### CONFIG
The `[CONFIG]` section contains basic configs for the service
- wait_time_secs [`int`] | The time between weather API requests and updating of the [ICAL Service](https://github.com/hamolicious/Google-ICAL-Weather-Integration/tree/master/ical_service)'s data

### LOCALE
The `[LOCALE]` section contains information about the location of the desired weather data

### ICONS
The `[ICONS]` section contains definitions for what the icons should look like.

### WEATHERCODES
The `[WEATHERCODES]` section contains a selection of the WW-WMO Weather Codes and their assigned icons and descriptions.

[^1]: May work with non "Google" calendars however that has not been tested
