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

features = ['sma','rsi','macd','macdSignal','adx','Middle bband','Lower bband','Upper bband','Parabolic sar','ema']
featuresList =[]

for feature in features:
    featuresList.append(data[feature])

#print(featuresList[0])

prices = data['price']
tY = np.array(prices).astype(np.float)
#print(Y.shape)
tX = np.array(featuresList).astype(np.float)
tX = tX.transpose()
#print(tX.shape)



class Net(nn.Module):
    def __init__(self):
        super().__init__()
        """ define layers here"""
        self.l1 = nn.Linear(10,5)
        self.l2 = nn.Linear(5,1)


    def forward(self, x):
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        return x


input = torch.from_numpy(tX).float()
target = torch.from_numpy(tY).float()

# define a tensor dataset
train_ds = TensorDataset(input,target)

# define dataloader
batch_size = 5
train_dl = DataLoader(train_ds,batch_size,shuffle = False)

net = Net()

optimizer = optim.SGD(net.parameters(),lr = .0000001)
#loss = nn.MSELoss()

epochs = 3

for epoch in range(epochs):
    for data in train_dl:
        X,y = data
        #pass forward
        out = net(X)
        net.zero_grad()
        #calc loss
        loss = F.mse_loss(out,y)


        loss.backward()
        optimizer.step()
        print(loss)

output = net(input.narrow(0,2000,2))
print(output)
