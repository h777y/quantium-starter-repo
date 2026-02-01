import csv

with open('../1)createNewCsv/daily_sales_data_0_with_sales.csv', newline='') as file: #opens the file
    reader = csv.reader(file) #csv.reader reads one row at a time

    with open('daily_sales_data_0deblot.csv', 'w', newline='') as outfile: #creates a new file
        writer = csv.writer(outfile)

        for row in reader:
            del row[0] # all three delete the first row each time the data gets shifted to the right
            del row[0]
            del row[0]
            writer.writerow(row)