import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import csv
import numpy as np
from torch.utils.data import TensorDataset, DataLoader


with open('testfile.csv','r') as file:
    csv_reader = csv.DictReader(file)
    data ={}
    for row in csv_reader:
        for key, value in row.items():
            data.setdefault(key, list()).append(value)

features = ['price','sma','rsi','macd','macdSignal','adx','Middle bband','Lower bband','Upper bband','Parabolic sar','ema']
featuresList =[]

for feature in features:
    featuresList.append(data[feature])


prices = data['price']
tY = np.array(prices).astype(np.float)
#print(Y.shape)
tX = np.array(featuresList).astype(np.float)
tX = tX.transpose()

trainExs =[]
trainYs = []

i =0
while i < 2047-21:
    tempEx = tX[i:i+12]
    tempEx = tempEx.flatten()
    tempEx = tempEx.tolist()
    trainExs.append(tempEx)

    i+=1

j =0
while j < 2047-21:
    tempY = tY[j+15:j+21]
    tempY = tempY.flatten()
    tempY = tempY.tolist()
    trainYs.append(tempY)
    j+=1

print(len(trainYs))
targets = torch.FloatTensor(trainYs)
inputs = torch.FloatTensor(trainExs)

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        '''
        self.l1 = nn.Linear(132,20)
        self.l2 = nn.Linear(20,15)
        self.l3 = nn.Linear(15,10)
        self.l4 = nn.Linear(10,6)
        '''
        self.l1 = nn.Linear(132,20)
        self.l2 = nn.Linear(20,6)


    def forward(self,x):
        '''
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = F.relu(self.l3(x))
        x = F.relu(self.l4(x))
        '''
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))

        return x


#print(inputs.shape)

inputMin = inputs.min(0,keepdim=True)[0]
inputMax = inputs.max(0,keepdim=True)[0]
#print(inputs.narrow(0,2000,2))

copyInputs= inputs
'''
min max normalization
copyInputs -= inputMin
copyInputs /= inputMax - inputMin
inputs = copyInputs
'''

copyInputs -= torch.mean(copyInputs,dim=0)
copyInputs /= torch.std(copyInputs,dim=0)
inputs = copyInputs


net = Net()
trainDS = TensorDataset(inputs,targets)

batch_size = 10

train_dl = DataLoader(trainDS,batch_size,shuffle = False)



optimizer = optim.SGD(net.parameters(), lr = 1e-5)

epochs = 200

lossFn = F.mse_loss


for epoch in range(epochs):
    for data in train_dl:
        X,y = data
        out = net(X)

        loss = lossFn(out,y)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
    print('Training loss: ', lossFn(net(inputs), targets))



with open('actualtestfile.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    testdata ={}
    for row in csv_reader:
        for key, value in row.items():
            testdata.setdefault(key, list()).append(value)

testfeatures = ['price','sma','rsi','macd','macdSignal','adx','Middle bband','Lower bband','Upper bband','Parabolic sar','ema']
testfeaturesList =[]

for feature in testfeatures:
    testfeaturesList.append(testdata[feature])


testprices = testdata['price']
testY = np.array(testprices).astype(np.float)
#print(Y.shape)
testX = np.array(testfeaturesList).astype(np.float)
testX = testX.transpose()


testXs = []
testYs = []
#print(testX.shape)
k = 20

while k < 3127 -21:
    temp = testX[k:k+12]
    temp = temp.flatten()
    temp = temp.tolist()
    testXs.append(temp)
    k+=1


l = 20

while l< 3127-21:
    tempTY = testY[l+15:l+21]
    tempTY = tempTY.flatten()
    tempTY = tempTY.tolist()
    testYs.append(tempTY)
    l+=1




testInputs = torch.FloatTensor(testXs)
testTargets = torch.FloatTensor(testYs)

#print(testTargets)

copyTestInputs = testInputs

copyTestInputs -= torch.mean(copyTestInputs,dim=0)
copyTestInputs /= torch.std(copyTestInputs,dim=0)
testInputs = copyTestInputs



testOutputs = net(testInputs)


#3086 guesses



print(testOutputs)
