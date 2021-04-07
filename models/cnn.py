import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import csv
import numpy as np
from torch.utils.data import TensorDataset, DataLoader

with open('C:\\Users\\17732\Documents\\TradingScheme\\data\\oneMinutePriceDataFinal.csv','r') as price_file:
    csv_reader = csv.DictReader(price_file)
    data={}
    for row in csv_reader:
        for key, value in row.items():
            data.setdefault(key, list()).append(value)
total = len(data['direction'])-1

x = []
tensor2 = torch.FloatTensor([[1],[0],[0]])
tensor1 = torch.FloatTensor([[0],[1],[0]])
tensor0 = torch.FloatTensor([[0],[0],[1]])

for i in range(5000):
    if (float(data['direction'][total-i]))==2:
        x.append(tensor2)
    elif (float(data['direction'][total-i]))==1:
        x.append(tensor1)
    elif (float(data['direction'][total-i]))==0:
        x.append(tensor0)

targets = x[0]

for i in range(1,len(x)):
    targets = torch.cat((targets,x[i]),dim=1)

#print(targets.shape)

with open('C:\\Users\\17732\\Documents\\TradingScheme\\data\\oneMinuteIndicatorDataFinal.csv','r') as indicator_file:
    csv_reader = csv.DictReader(indicator_file)
    indicatorData ={}
    for row in csv_reader:
        for key, value in row.items():
            indicatorData.setdefault(key,list()).append(value)

features =['adx','ema','rsi','sar','vwap','upper_band','middle_band','lower_band','macd','macd_signal','macd_hist','tenkan_sen','kijun_sen','senkou_span_a','senkou_span_b','chikou_span','open','high','low','close','volume']
featuresList=[]

for feature in features:
    indicatorData[feature].reverse()
    temp = [float(num) for num in indicatorData[feature]]
    featuresList.append(temp)

tempX = torch.FloatTensor(featuresList)
#print(tempX.shape)
tempX -= torch.reshape(torch.mean(tempX,dim=1),(21,1))
tempX /= torch.reshape(torch.std(tempX,dim=1),(21,1))
X = tempX
X = X.narrow(1,0,5000)

print(X.shape)
print(targets.shape)


class Cnn(nn.Module):
    def __init__(self):


        super().__init__()
        self.convLayer1 = nn.Conv1d(in_channels=21, out_channels=30,kernel_size=4)
        self.relu = nn.ReLU()
        self.ltConv= nn.Conv1d(10,1,kernel_size=1)
        self.mtConv= nn.Conv1d(10,1,kernel_size=1)
        self.stConv= nn.Conv1d(10,1,kernel_size=1)
        self.linear= nn.Linear(36,3)
        #self.outLayer= nn.Linear()

    def forward(self, x):
        x = self.relu(self.convLayer1(x))
        #print(x.shape)
        lt = torch.split(x,10,dim=1)[0]
        #print(lt.shape)
        mt = torch.split(x,10,dim=1)[1]
        st = torch.split(x,10,dim=1)[2]

        ltConv = self.relu(self.ltConv(lt))
        #print(ltConv.shape)
        mtConv = self.relu(self.mtConv(mt))
        #print(mtConv.shape)
        stConv = self.relu(self.stConv(st))
        #print(stConv.shape)

        x = torch.cat((ltConv,mtConv,stConv),1)
        #print(x.shape)
        x = torch.flatten(x)

        x = F.softmax(self.linear(x),dim=0)

        return x



net = Cnn()
learning_rate = .0001
epochs = 200

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)


#trainDS = TensorDataset(X,targets)
#batch_size = 1
#train_dl = DataLoader(trainDS,batch_size,shuffle = False)
#optimizer = optim.SGD(net.parameters(), lr = 1e-5)

#test = torch.rand(1,21,15)
