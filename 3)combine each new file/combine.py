import csv

files = ['0.csv', '1.csv', '2.csv',]
with open('pink_morselssssssss.csv', "w", newline="") as outfile:
    writer = csv.writer(outfile)
    for path in files:
        with open(path, newline="") as file: #each file is opened and passed as the iteration(path) goes up by one
            reader = csv.reader(file, delimiter=',')
            header = next(reader)
            writer.writerow(header)
            for row in reader:
                writer.writerow(row)