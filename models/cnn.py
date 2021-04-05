import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import csv
import numpy as np
from torch.utils.data import TensorDataset, DataLoader

with open('oneMinutePriceDataFinal.csv','r') as data_file:
    csv_reader = csv.DictReader(data_file)
    data={}
    for row in csv_reader:
        for key, value in row.items():
            data.setdefault(key, list()).append(value)

print('hi')

'''
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
        print(x.shape)
        lt = torch.split(x,10,dim=1)[0]
        print(lt.shape)
        mt = torch.split(x,10,dim=1)[1]
        st = torch.split(x,10,dim=1)[2]

        ltConv = self.relu(self.ltConv(lt))
        print(ltConv.shape)
        mtConv = self.relu(self.mtConv(mt))
        print(mtConv.shape)
        stConv = self.relu(self.stConv(st))
        print(stConv.shape)

        x = torch.cat((ltConv,mtConv,stConv),1)
        print(x.shape)
        x = torch.flatten(x)

        x = F.softmax(self.linear(x),dim=0)

        return x

net = Cnn()
test = torch.rand(1,21,15)
'''
