""" finally a some good data"""

import requests
import json
import csv
import time

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

oneMinList=[]

key = '21b4fb6f0acf4251a970af9eff02e03e'
sym = 'TQQQ'
start_date = '2020-12-18 15:08:00',
end_date = '2021-01-02',
interval = '1min'

params={
    'symbol':sym,
    'interval':interval,
    'start_date':start_date,
    'end_date':end_date,
    'apikey':key
}

"""ADX one min data"""

responseADX = requests.get('https://api.twelvedata.com/adx?',params= params)
dictresponseADX = (responseADX.json())
oneMinList.append(dictresponseADX['values'])


"""EMA one min data"""

responseEMA = requests.get('https://api.twelvedata.com/ema?',params= params)
dictresponseEMA = (responseEMA.json())
oneMinList.append(dictresponseEMA['values'])


"""RSI one min data"""

responseRSI = requests.get('https://api.twelvedata.com/rsi?',params= params)
dictresponseRSI = (responseRSI.json())
oneMinList.append(dictresponseRSI['values'])

"""SAR one min data"""

responseSAR = requests.get('https://api.twelvedata.com/sar?',params= params)
dictresponseSAR = (responseSAR.json())
oneMinList.append(dictresponseSAR['values'])

"""VWAP one min data"""

responseVWAP = requests.get('https://api.twelvedata.com/vwap?',params= params)
dictresponseVWAP = (responseVWAP.json())
oneMinList.append(dictresponseVWAP['values'])

"""BBANDS one min data"""

responseBBANDS = requests.get('https://api.twelvedata.com/bbands?',params= params)
dictresponseBBANDS = (responseBBANDS.json())
oneMinList.append(dictresponseBBANDS['values'])


"""MACD one min data"""

responseMACD = requests.get('https://api.twelvedata.com/macd?',params= params)
dictresponseMACD = (responseMACD.json())
oneMinList.append(dictresponseMACD['values'])

"""ICHIMOKU one min data"""

responseICHIMOKU = requests.get('https://api.twelvedata.com/ichimoku?',params= params)
dictresponseICHIMOKU = (responseICHIMOKU.json())
oneMinList.append(dictresponseICHIMOKU['values'])


indicatorValues=[]
for i in range(2993):
    newRow = []
    newRow.append(oneMinList[0][i]['datetime'])
    for j in range(len(oneMinList)):
        for key in oneMinList[j][i]:
            if key != 'datetime':
                newRow.append(oneMinList[j][i][key])
    indicatorValues.append(newRow)


fieldnames = ['datetime','adx','ema','rsi','sar','vwap','upper_band','middle_band','lower_band','macd','macd_signal','macd_hist','tenkan_sen','kijun_sen','senkou_span_a','senkou_span_b','chikou_span']

with open('oneMinuteIndicatorData19.csv','w') as newFile:
    write = csv.writer(newFile, lineterminator='\n')
    write.writerow(fieldnames)
    write.writerows(indicatorValues)

#jprint(response.json())
#print(dictresponse)
