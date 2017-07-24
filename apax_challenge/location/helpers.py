import requests
import json


def get_weather(lat,lon):
	""" Utility function to get the weather data from the NWS API

	Requres lat/lon. Just a get request to the api server
	"""
	URL = 'http://api.weather.gov/points/{},{}/forecast'.format(lat, lon)

	res = requests.get(URL)
	if res.status_code == 200:
		weather = json.loads(res.text)
		if weather['properties']['periods'][0]['isDaytime']:
			h_i = 0
			l_i = 1
		else:
			h_i = 1
			l_i = 0

		return {'high': weather['properties']['periods'][h_i]['temperature'],
			'low': weather['properties']['periods'][l_i]['temperature'],
			'wind_speed': weather['properties']['periods'][0]['windSpeed'],
			'short_forecast': weather['properties']['periods'][0]['shortForecast'],
			'detailed_forecast': weather['properties']['periods'][0]['detailedForecast'],}
	else:
		return None
