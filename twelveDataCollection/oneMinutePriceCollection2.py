""" finally a some good data"""

import requests
import json
import csv
import time


oneMinList=[]

key = '21b4fb6f0acf4251a970af9eff02e03e'
sym = 'TQQQ'
interval = '1min'


"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2021-02-15',
    'end_date':'2021-02-27',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2021-02-01',
    'end_date':'2021-02-13',
    'apikey':key
}
response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2021-01-18',
    'end_date':'2021-01-30',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2021-01-04',
    'end_date':'2021-01-16',
    'apikey':key
}
response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-12-21',
    'end_date':'2021-01-02',
    'apikey':key
}
response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-12-07',
    'end_date':'2020-12-19',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data 02"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-11-23',
    'end_date':'2020-12-05',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])


"""price one min data 01"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-11-09',
    'end_date':'2020-11-21',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

minutePriceList=[]

for i in range(len(oneMinList)):
    for j in range(len(oneMinList[i])):
        temp=[]
        temp.append(oneMinList[i][j]['datetime'])
        temp.append(oneMinList[i][j]['open'])
        temp.append(oneMinList[i][j]['high'])
        temp.append(oneMinList[i][j]['low'])
        temp.append(oneMinList[i][j]['close'])
        temp.append(oneMinList[i][j]['volume'])
        minutePriceList.append(temp)

fieldnames=['datetime','open','high','low','close','volume']
with open('oneMinutePriceDataex.csv','w') as newFile:
    write = csv.writer(newFile, lineterminator='\n')
    write.writerow(fieldnames)
    write.writerows(minutePriceList)



#print(oneMinList)
