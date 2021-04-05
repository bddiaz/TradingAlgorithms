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
    'start_date':'2020-07-06',
    'end_date':'2020-07-18',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-06-22',
    'end_date':'2020-07-04',
    'apikey':key
}
response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-06-08',
    'end_date':'2020-06-20',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-05-25',
    'end_date':'2020-06-06',
    'apikey':key
}
response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-05-11',
    'end_date':'2020-05-23',
    'apikey':key
}
response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-04-27',
    'end_date':'2020-05-09',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])

"""price one min data 02"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-04-13',
    'end_date':'2020-04-25',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])


"""price one min data 01"""
params={
    'symbol':sym,
    'interval':interval,
    'start_date':'2020-03-30',
    'end_date':'2020-04-11',
    'apikey':key
}

response = requests.get('https://api.twelvedata.com/time_series?',params= params)
dictresponse = (response.json())
oneMinList.append(dictresponse['values'])


'''
"""price one min data"""
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


"""price one min data"""
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
'''
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
with open('oneMinutePriceData.csv','w') as newFile:
    write = csv.writer(newFile, lineterminator='\n')
    write.writerow(fieldnames)
    write.writerows(minutePriceList)



#print(oneMinList)
