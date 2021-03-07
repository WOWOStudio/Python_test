import csv

with open('the_csv.csv',newline='',encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
