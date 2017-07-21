import requests
import json


def get_weather(lat,lon):
	URL = 'http://api.weather.gov/points/{},{}/forecast'.format(lat, lon)

	res = requests.get(URL)
	if res.status_code == 200:
		weather = json.loads(res.text)
		return {'high': weather['properties']['periods'][0]['temperature'],
			'low': weather['properties']['periods'][1]['temperature'],
			'wind_speed': weather['properties']['periods'][0]['windSpeed'],
			'short_forecast': weather['properties']['periods'][0]['shortForecast'],
			'detailed_forecast': weather['properties']['periods'][0]['detailedForecast'],}
	else:
		return None
