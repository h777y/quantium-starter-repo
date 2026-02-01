import csv

files = ['data/daily_sales_data_0deblot.csv', 'data/daily_sales_data_1deblot.csv', 'data/daily_sales_data_0deblot.csv',]
with open('pink_morsels', "w", newline="") as outfile:
    writer = csv.writer(outfile)
    for path in files:
        with open(path, newline="") as file: #each file is opened and passed as the iteration(path) goes up by one
            reader = csv.reader(file, delimiter=',')
            header = next(reader)
            writer.writerow(header)
            for row in reader:
                writer.writerow(row)