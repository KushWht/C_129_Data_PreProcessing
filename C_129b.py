import csv

dataset_1 = []
dataset_2 = []

with open('C:\\Users\\HP\\Documents\\Python Projects\\C_129_PRO\\unit_converted_stars.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        dataset_1.append(row)

with open('C:\\Users\\HP\\Documents\\Python Projects\\C_129_PRO\\bright_stars.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        dataset_2.append(row)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = headers_1 + headers_2

planet_data = []

for i in planet_data_1:
    planet_data.append(i)

for j in planet_data_2:
    planet_data.append(i)

with open("total_stars.csv", "a+") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(planet_data)