import csv

with open('data/daily_sales_data_2_with_sales.csv', newline='') as file:
    reader = csv.reader(file)
    with open('data/daily_sales_data_2_deblotted.csv', newline ='') as outfile:
        writer = csv.writer(outfile)
        for row in reader:
            del row[0]
