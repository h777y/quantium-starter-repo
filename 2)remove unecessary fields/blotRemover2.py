import csv

with open('../1)createNewCsv/daily_sales_data_2_with_sales.csv', newline='') as file: #opens the file
    reader = csv.reader(file) #csv.reader read one row at a time

    with open('daily_sales_data_2deblot.csv', 'w', newline='') as outfile: #opens the file as write only
        writer = csv.writer(outfile)

        for row in reader:
            del row[0]
            del row[0]
            del row[0]
            writer.writerow(row)