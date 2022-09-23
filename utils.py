import requests
import json
from datetime import datetime

address = "http://192.168.1.182:1987"

logfile = "/home/nocjetson/Analytics-VIW/analyticsDebugLog.txt"
requestFile = "/home/nocjetson/Analytics-VIW/analyticsRequestLog.txt"




def check_status(response, *args, **kwargs):

   

    if (response.status_code == requests.codes.ok):
        result = "Informação de evento enviada com sucesso!"
    else:
        result = "Problema na requisição à api."
        with open(logfile, "a") as myfile:
            myfile.write("\n[" + str(datetime.now()) +
                         "] - Problema na requisição à api. - ")


def sendEvent(eventType):
    print("Enviando informações do evento")
    payload = {'type': eventType} 

    requests.post(address + "/Reader", json=payload)





 