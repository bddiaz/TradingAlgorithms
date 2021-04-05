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
    'start_date':'2020-10-26',
    'end_date':'2020-11-07',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-10-12',
    'end_date':'2020-10-24',
    'apikey':key
}
response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-09-28',
    'end_date':'2020-10-10',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-09-14',
    'end_date':'2020-09-26',
    'apikey':key
}
response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-08-31',
    'end_date':'2020-09-12',
    'apikey':key
}
response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-08-17',
    'end_date':'2020-08-29',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data 02"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-08-03',
    'end_date':'2020-08-15',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])


"""price one min data 01"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-07-20',
    'end_date':'2020-08-01',
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
with open('oneMinutePriceData1.csv','w') as newFile:
    write = csv.writer(newFile, lineterminator='\n')
    write.writerow(fieldnames)
    write.writerows(minutePriceList)



#print(oneMinList)
