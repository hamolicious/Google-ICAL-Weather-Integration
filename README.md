# Google-ICAL-Weather-Integration
Uses a [weather api](https://open-meteo.com/en) to request weather data for the next 7 days and integrates it into Google Calendar [^1]


## How to run


## Configuration
The Calendar Service has a [config file](calendar_service/calendar_service/config.hamconf):

- wait_time_secs [`int`] | The time between weather API requests and updating of the [ICAL Service](https://github.com/hamolicious/Google-ICAL-Weather-Integration/tree/master/ical_service)'s data

The `[ICONS]` section contains definitions for what the icons should look like and the `[WEATHERCODES]` section contains a selection of the WW WMO Weather Codes and their assigned icons and descriptions.

[^1]: May work with non "Google" calendars however that has not been tested
