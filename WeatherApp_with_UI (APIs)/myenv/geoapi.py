import requests
import json
# api source: https://www.geojs.io/docs/v1/endpoints/geo/
def get_external_ip():
    response = requests.get('http://api.ipify.org')
    return response.text

external_ip = get_external_ip()
print("Your external IP is:", external_ip)


def get_long_lat(external_ip):
    url = "https://get.geojs.io/v1/ip/geo/%s.json"%external_ip
    response = requests.get(url)
    jj = response.json()
    country = jj["country"]
    city = jj["city"]
    print (country, city)
    #print (response.text)
    return response.json(), country, city

jj,country,city = get_long_lat(external_ip)
long = jj["longitude"]
lat = jj["latitude"] 
result = "Your country is %s"%country+" and your city is "+city+"."
print (result)