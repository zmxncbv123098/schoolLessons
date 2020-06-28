import csv
#
# with open('exportdata.csv', "r") as csvfile:
#     csvfile.readline()
#     spamreader = csv.reader(csvfile)
#     for row in spamreader:
#         if int(row[2][1:].replace(",","")) > 999999999999:
#             print(row[0])


with open('weather-2014-05-01.csv', "r") as csvfile:
    csvfile.readline()
    spamreader = csv.reader(csvfile)
    mini = 1000
    for row in spamreader:
        if float(row[1]) < mini:
            mini = float(row[1])
    print(mini)