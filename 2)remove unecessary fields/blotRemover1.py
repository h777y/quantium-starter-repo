import csv

with open('../1)createNewCsv/daily_sales_data_1_with_sales.csv', newline='') as file: #opens the file
    reader = csv.reader(file)

    with open('daily_sales_data_1deblot.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        for row in reader:
            del row[0]
            del row[0]
            del row[0]
            writer.writerow(row)