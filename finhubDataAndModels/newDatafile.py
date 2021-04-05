import csv


with open('indicatordatafile.csv','r') as file:
    csv_reader = csv.DictReader(file)
    data ={}
    for row in csv_reader:
        for key, value in row.items():
            data.setdefault(key, list()).append(value)

features = ['o','c','h','l','rsi','macd','macdSignal','macdHist','adx','Middle bband','Lower bband','Upper bband','Parabolic sar','ema']
featuresList =[]

for feature in features:
    featuresList.append(data[feature])

oList = [float(i) for i in data['o']]
cList = [float(i) for i in data['c']]
hList = [float(i) for i in data['h']]
lList = [float(i) for i in data['l']]

''' macd buy and sell signals'''

macdBuySellSignalList =[]
macdStrengthSignalList =[]
macdList = [float(i) for i in data['macd']]
macdSignalList =[float(i) for i in data['macdSignal']]
macdHistList = [float(i) for i in data['macdHist']]

for i in range(len(macdList))[19:]:
    if macdList[i] > macdSignalList[i]:
        macdBuySellSignalList.append(1)
    else:
        macdBuySellSignalList.append(0)

'''
TO DO:
macd trend stength signals.

NEED INPUT FROM ISSA

for i in range(len(macdList))[19]:
    if
'''



''' rsi buy and sell signals'''

rsiBuySellSignalList =[]
rsiList = [float(i) for i in data['rsi']]
rsiStrengthSignalList =[]
for i in range(len(rsiList))[19:]:
    #print(rsiList[i])
    if rsiList[i] < 30:

        rsiBuySellSignalList.append(1)
    if rsiList[i] > 70:
        #print(rsiList[i])
        rsiBuySellSignalList.append(0)
    if rsiList[i] > 30 and rsiList[i] < 70:
        rsiBuySellSignalList.append(.5)


''' sar buy and sell signals'''

sarBuySellSignalList = []
sarList = [float(i) for i in data['Parabolic sar']]

for i in range(len(sarList))[19:]:
    if sarList[i] < min([oList[i],cList[i]]):
        sarBuySellSignalList.append(1)
    if sarList[i] > max([oList[i],cList[i]]):
        sarBuySellSignalList.append(0)
    if sarList[i] > min([oList[i],cList[i]]) and sarList[i] < max([oList[i],cList[i]]):
        sarBuySellSignalList.append(.5)



''' bollinger bands buy and sell signals'''

middlebandList =[float(i) for i in data['Middle bband']]
upperbandList =[float(i) for i in data['Upper bband']]
lowerbandList =[float(i) for i in data['Lower bband']]

bbandBuySellSignals=[]

for i in range(len(middlebandList))[19:]:
    if lowerbandList[i] > max([oList[i],cList[i]]):
        bbandBuySellSignals.append(1)
    if upperbandList[i] < min([oList[i],cList[i]]):
        bbandBuySellSignals.append(0)


print(bbandBuySellSignals)
