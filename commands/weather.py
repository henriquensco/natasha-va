#coding: UTF-8
import urllib.request as request
from urllib.error import URLError, HTTPError
import json


def previsaoDoTempo():
    url = "https://api.hgbrasil.com/weather?woeid=450398"

    try:

        data = request.urlopen(url)
        data = data.read().decode("UTF-8")
        
        data = json.loads(data)
        
        temp_max = data["results"]["forecast"][0]["max"]
        temp_min = data["results"]["forecast"][0]["min"]
        description = data["results"]["forecast"][0]["description"]
        
        result = "{desc} com máxima de {max} e mínima de {min} graus".format(desc=description, max=temp_max, min=temp_min)
        
        return result
        
    except HTTPError as e:
        print(e.status, e.reason)
    except URLError as e:
        print(e.reason)

previsaoDoTempo()