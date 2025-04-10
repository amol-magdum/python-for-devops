import csv

# Path to the CSV file
csv_file = 'example.csv'

# DictReader will consider first row as keys, which makes reading csv much easier
# if first row doesn't have keys the provide those in parameters
    # DistReader(csvfile, ['1_col','2_row','3_row'])
    
csvfile = open('example.csv')
csvreader = csv.DictReader(csvfile)
exampleData = list(csvreader)

print(exampleData[1])
