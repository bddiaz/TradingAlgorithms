import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import csv
import numpy as np
from torch.utils.data import TensorDataset, DataLoader, Dataset


'''
get targets from csv file
'''

with open('C:\\Users\\17732\Documents\\TradingScheme\\data\\oneMinutePriceDataFinal.csv','r') as price_file:
    csv_reader = csv.DictReader(price_file)
    data={}
    for row in csv_reader:
        for key, value in row.items():
            data.setdefault(key, list()).append(value)
total = len(data['direction'])-1

x = []
tensor2 = torch.Tensor([2])
tensor1 = torch.FloatTensor([1])
tensor0 = torch.FloatTensor([0])

for i in range(15000):
    if (float(data['direction'][total-i]))==2:
        x.append(tensor2)
    elif (float(data['direction'][total-i]))==1:
        x.append(tensor1)
    elif (float(data['direction'][total-i]))==0:
        x.append(tensor0)

targets = x[0]


for i in range(1,len(x)):
    targets = torch.cat((targets,x[i]),dim=0)



#print(targets)
'''
get features from csv file (indciator data and price data)
'''

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
tempX -= torch.reshape(torch.mean(tempX,dim=1),(21,1))
tempX /= torch.reshape(torch.std(tempX,dim=1),(21,1))
X = tempX

# limit to first 5000 examples
X = X.narrow(1,0,15000)
X = torch.transpose(X,0,1)



''' CNN model '''


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

        lt = torch.split(x,10,dim=1)[0]
        mt = torch.split(x,10,dim=1)[1]
        st = torch.split(x,10,dim=1)[2]

        ltConv = self.relu(self.ltConv(lt))
        mtConv = self.relu(self.mtConv(mt))
        stConv = self.relu(self.stConv(st))

        x = torch.cat((ltConv,mtConv,stConv),1)
        x = torch.flatten(x)
        #x = F.softmax(self.linear(x),dim=0)
        x = self.linear(x)

        return x

''' custom data set class'''

class TimeseriesDataset(Dataset):
    def __init__(self, X, y, seq_len=1):
        self.X = X
        self.y = y
        self.seq_len = seq_len

    def __len__(self):
        return self.X.__len__() - (self.seq_len-1)

    def __getitem__(self, index):
        return (self.X[index:index+self.seq_len], self.y[index+self.seq_len-1])




batch_size=4
trainDS =  TimeseriesDataset(X,targets,seq_len=15)
trainDL = DataLoader(trainDS,batch_size,shuffle=False)



net = Cnn()
learning_rate = .00001
epochs = 10
n_total_steps = len(trainDL)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)

for epoch in range(epochs):
    for i, (features, targets) in enumerate(trainDL):
        features=torch.transpose(features,1,2)
        targets = targets.type(torch.LongTensor)
        outputs= net(features)
        outputs = torch.reshape(outputs,(1,3))
        #outputs = outputs.type(torch.LongTensor)
        #print(outputs.shape)
        loss = criterion(outputs,targets)


        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (i+1) % 2000 == 0:
            print (f'Epoch [{epoch+1}/{epochs}], Step [{i+1}/{n_total_steps}], Loss: {loss.item():.4f}')

print('finish training')

#testout = net(test)
#print(testout)
