# -*- coding: utf-8 -*

import requests
import csv
import time
import json
from datetime import datetime

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# 91 days of stats


resol = "5"
#start date is 06/01/2020 at 8:30 am ct


startDate = "1590998400"
#end date is 06/20/2020 at 3pm ct
endDate = "1593504000"
sym = "TQQQ"
key = "bu8cu4f48v6oles0b2pg"


parameters = {
        "symbol": sym,
        "resolution":resol,
        "from":startDate,
        "to":endDate,
        "indicator":"sma",
        "token":key
        }
parameters1 = {
    "symbol": sym,
    "resolution": resol,
    "from":startDate,
    "to":endDate,
    "indicator":"rsi",
    "token": key
}
parameters2 = {
    "symbol": sym,
    "resolution": resol,
    "from":startDate,
    "to":endDate,
    "indicator":"macd",
    "token": key
}
parameters3 = {
    "symbol": sym,
    "resolution": resol,
    "from":startDate,
    "to":endDate,
    "indicator":"adx",
    "token": key
}
parameters4 = {
    "symbol": sym,
    "resolution": resol,
    "from":startDate,
    "to":"1607659200",
    "indicator":"bbands",
    "token": key
}
parameters5 = {
    "symbol": sym,
    "resolution": resol,
    "from":startDate,
    "to":endDate,
    "indicator":"sar",
    "token": key
}
parameters6 = {
    "symbol": sym,
    "resolution": resol,
    "from":startDate,
    "to":endDate,
    "indicator":"ema",
    "token": key
}

response = requests.get("https://finnhub.io/api/v1/indicator?",params = parameters)
response1 = requests.get("https://finnhub.io/api/v1/indicator?",params= parameters1)
response2 = requests.get("https://finnhub.io/api/v1/indicator?",params= parameters2)
response3 = requests.get("https://finnhub.io/api/v1/indicator?",params= parameters3)
response4 = requests.get("https://finnhub.io/api/v1/indicator?",params= parameters4)
response5 = requests.get("https://finnhub.io/api/v1/indicator?",params= parameters5)
response6 = requests.get("https://finnhub.io/api/v1/indicator?",params= parameters6)

dictresponse = (response.json())
dictresponse1 = (response1.json())
dictresponse2 = (response2.json())
dictresponse3 = (response3.json())
dictresponse4 = (response4.json())
dictresponse5 = (response5.json())
dictresponse6 = (response6.json())

timeCopy = dictresponse1['t']
newTime =[]
for i in range(len(timeCopy)):
    newTime.append(datetime.utcfromtimestamp(int(timeCopy[i])).strftime('%Y-%m-%d- %H:%M:%S'))

newDict = {
    'time':newTime,
    'price':dictresponse['c'],
    'sma':dictresponse['sma'],
    'rsi':dictresponse1['rsi'],
    'macd':dictresponse2['macd'],
    'macdSignal':dictresponse2['macdSignal'],
    'adx':dictresponse3['adx'],
    'Middle bband':dictresponse4['middleband'],
    'Lower bband':dictresponse4['lowerband'],
    'Upper bband':dictresponse4['upperband'],
    'Parabolic sar':dictresponse5['sar'],
    'ema':dictresponse6['ema']

}

with open('testfile.csv','w') as newFile:

    writer = csv.writer(newFile, lineterminator='\n')
    writer.writerow(newDict.keys())
    writer.writerows(zip(*newDict.values()))

#jprint(response.json())
