## Overview

Weather loader/viewer example program in python/django/jquery/bootstrap

## Operation

Anyone can create a user with a username/password. I find that the django authentication system is as easy as anything so I just used it. So you have to put in a password.

Creating a user will log you in. From there, you can add locations. The location system is very simple, and only accepts zipcodes. The zipcodes are looked up in the google maps api to get location information.

Each location will show up in your list. Locations can only be added once. If a different user has already added a location, you will see data for it. If not, the location data will be initially blank.

Refresh buttons are provided for each data row. If JS is enabled the refresh will be done by AJAX. Otherwise, a pageload will cover it. There is a convenient bug in the JSon generator view that makes it slightly more obvious when a location refresh has completed because the date format changes.

Clicking on a location in the table will show a detail view of that location, which shows a slightly more detailed forcast.

## Discussion

### Location Data and API

I used the google maps API to get location data. I grabbed a python library for looking up zipcodes first (zipcode on pip) but then realized it was loading an sqlite database which wasn't super convenient. Since we're hitting a weather API anyway, the maps API was an easy way to get location data. Looking up locations by name would likely be possible this way as well.

I avoid hitting the location API excessively by storing each location only once. Only when the location is initially added with the maps API be hit.

### Weather API

The National Weather Service provides an API for their weather data. Since that's public data I used that. It was also a very simple interface that just needed lat/lon.

The weather API is hit on every `refresh`. When the location detail page is requested the weather is updated as well, unless it has already been updated within 5 minutes.

### Database

I used the django ORM for this project since I was in django anyway. Since I built it in django, and this project isn't expanding into anything, I let django default to sqlite rather than configuring MySQL.

## Known Issues

- There is no option to delete, either users or locations.

- Loading the weather using the AJAX call on the user page styles the date/time differently from the django template. The obvious fix would be to let django style it before the send, but it provides a convenient way to see the ajax call succeed.

- No error checking on the API calls, and minimal error checking otherwise

- No tests