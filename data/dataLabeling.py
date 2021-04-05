import csv

with open('oneMinutePriceDataFinal.csv','r') as data_file:
    csv_reader = csv.DictReader(data_file)
    data={}
    for row in csv_reader:
        for key, value in row.items():
            data.setdefault(key, list()).append(value)


print(data['direction'])
