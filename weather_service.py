"""For the Morning Assistant raspberry pi project, this file
will contain the python script in which the weather data will be gathered"""

# The first step is to import the http requests 
import requests

# afterwards, I'll test using my personal api key and city, then switch to variables

apikey = "xxxxxxxx"
City = "Houston"
# I will then construct endpoint url and send the GET request

# convert the units to farenheit since scientific data uses Kelvin

# get the json response and translate it into python, and finally display the neatly formatted data

