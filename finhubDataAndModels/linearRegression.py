import csv
import numpy as np
import torch

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
Y = np.array(prices).astype(np.float)
#print(Y.shape)
X = np.array(featuresList).astype(np.float)
X = X.transpose()
#print(X.shape)


''' model for predictions'''
def model(x):
    return x @ w.t() + b


''' mean squared error loss function'''
def lossFn(t1,t2):
    dif = t1-t2
    return torch.sum(dif*dif)/dif.numel()

input = torch.from_numpy(X).float()
out = torch.from_numpy(Y).float()


w = torch.randn(1,10,requires_grad = True)
b = torch.randn(1,1,requires_grad = True)

for i in range(100):
    result = model(input)
    error = lossFn(result,out)
    error.backward()
    print(error)
    print(i)
    with torch.no_grad():
        w -= w.grad * 1e-6
        b -= b.grad * 1e-6
        w.grad.zero_()
        b.grad.zero_()


print(error)
print(result)
print(out)
