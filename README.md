## Setup

This can be run from the manage.py server. I usually set up gunicorn for production projects, which this is not.

Don't forget to install `requirements.txt`

This uses sqlite throught the django ORM. Feel free to configure a different DB, but the default settings are left in place.

## Overview

Weather loader/viewer example program in python/django/jquery/bootstrap

## Operation

Anyone can create a user with a username/password. I find that the django authentication system is as easy as anything so I just used that, so you have to put in a password.

Creating a user will log you in. From there, you can add locations. The location system is very simple, and only accepts zipcodes. The zipcodes are looked up in the google maps api to get location information.

Each location will show up in your list. Locations can only be added once. If a different user has already added a location, you will see data for it. If not, the location data will be initially blank.

Refresh buttons are provided for each data row. If JS is enabled the refresh will be done by AJAX. Otherwise, a pageload will cover it. There is a convenient bug in the JSon generator view that makes it slightly more obvious when a location refresh has completed because the date format changes.

Clicking on a location in the table will show a detail view of that location, which shows a slightly more detailed forcast.

## Discussion

### Person and django auth

Since django provides an easy login system, I put that in for managing users. Howwever I typically wrap the login user with a class local to my project. This protects against me modifying the user system in some way, and only adds a bit of hassle. I called that class `Person`. `Person` has some views and URLs but doesn't provide much in its model.

### Location Data and API

I used the google maps API to get location data. I grabbed a python library for looking up zipcodes first (zipcode on pip) but then realized it was loading an sqlite database which wasn't super convenient. Since we're hitting a weather API anyway, the maps API was an easy way to get location data (The weather API wants lat/lon, and it seems a stretch to ask a user for that). Looking up locations by name would likely be possible this way as well. Since we're getting the data anyway, I added a little of that data to display as well.

I avoid hitting the location API excessively by storing each location only once. The api `GET` is only requested when the location is initially added.

### Weather API

The National Weather Service provides an API for their weather data. Since that's public data I used that (your tax dollars at work). It was also a very simple interface that just needed lat/lon.

The weather API is hit on every `refresh`. When the location detail page is requested the weather is updated as well, unless it has already been updated within 5 minutes.

### Database

I used the django ORM for this project since I was in django anyway. Since I built it in django, and this project isn't expanding into anything, I let django default to sqlite rather than configuring MySQL.

### Additional Dependencies

I'm not a designer so I used bootstrap for this project. Even if I were a designer I'd probably use it since it makes layouts easy. I also grabbed the `django-bootstrap3` PyPi lib which gives easy CDN links. This was the first time I'd used the `django-bootstrap3` lib and it was fine, but I'm not sure it was worth the requirement.

For the front end I used JQuery, so I also put a CDN link in. You can find these in `apax_challenge/person/templates/person/base.html` by the way.


## Known Issues

- There is no option to delete, either users or locations.

- Loading the weather using the AJAX call on the user page styles the date/time differently from the django template. The obvious fix would be to let django style it before the send, but it provides a convenient way to see the ajax call succeed.

- No error checking on the API calls, and minimal error checking otherwise

- No tests