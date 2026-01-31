import csv

with open('data/daily_sales_data_0.csv', newline='') as file: #opens the file
    reader = csv.reader(file) #csv.reader read one row at a time
    header = next(reader) #end of the read row

    header.append("Sales") #appends on the end of the row

    with open('data/daily_sales_data_0_with_sales.csv', 'w', newline='') as outfile: #opens the file as write only
        writer = csv.writer(outfile)
        writer.writerow(header) #writes the headers


        for row in reader:

            money = row[1][1:]
            salesV = float(money) * float(row[2])
            print(money)
            if row[0] == "pink morsel":
                row.append("$" + str(salesV) + "0")
                writer.writerow(row) #pnly rows that pass the test get written

