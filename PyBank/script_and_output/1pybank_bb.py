# modules
import os
import csv

# multi file differenciation list to read and process multiple similar files
mfile = ['1', '2']

# loop multiple files
for file in mfile:

    # get csv data sets
    bankdataCSV = os.path.join('..', 'raw_data', 'budget_data_' + file + '.csv')

    # create data lists to be appended for later manipulation
    dates = []
    revenue = []
    revchange = []

    # read csv
    with open(bankdataCSV, "r") as csvfile:
        
        # define delimiter and variable to hold date
        csvReader = csv.reader(csvfile, delimiter=',')

        # tell it to skip headers
        next(csvReader, None)

        # loop compile dates and revenue lists from csv
        for row in csvReader:

            dates.append(row[0])
            revenue.append(int(row[1]))

        # count months
        mocount = len(dates)

        # populate revchage list accounting for the fact there is no comparison after x+1 is the last value
        for x in range(len(revenue)-1):
            revchange.append(revenue[x] - revenue[x+1])

        
        # drop last date from list because we have no subsequent date for revchange comparison
        dates.pop(-1)

        # zip amended dates and generated revchenge lists into dictionary
        revchangedates = dict(zip(dates, revchange))
        
        # print analysis to terminal referencing the dictionary
        print("Financial Analysis - " + "budget_data_" + file)
        print("-------------------------------------")
        print("Total Months: " + str(mocount))
        print("Total Revenue: $" + str(sum(revenue)))
        print("Average Revenue Change: $" + str(round(sum(revchange)/len(revchange), 2)))
        print("Greatest Increase in Revenue: " + list(revchangedates.keys())[list(revchangedates.values()).index(max(revchange))] + " $" + str(max(revchange)))
        print("Greatest Decrease in Revenue: " + list(revchangedates.keys())[list(revchangedates.values()).index(min(revchange))] + " $" + str(min(revchange)))

        # create and write text files
        f = open("budget_data_" + file + ".txt", "w")

        f.writelines("Financial Analysis - " + "budget_data_" + file + "\n")
        f.writelines("-------------------------------------" + "\n")
        f.writelines("Total Months: " + str(mocount) + "\n")
        f.writelines("Total Revenue: $" + str(sum(revenue)) + "\n")
        f.writelines("Average Revenue Change: $" + str(round(sum(revchange)/len(revchange), 2)) + "\n")
        f.writelines("Greatest Increase in Revenue: " + list(revchangedates.keys())[list(revchangedates.values()).index(max(revchange))] + " $" + str(max(revchange)) + "\n")
        f.writelines("Greatest Decrease in Revenue: " + list(revchangedates.keys())[list(revchangedates.values()).index(min(revchange))] + " $" + str(min(revchange)) + "\n")
        f.close()

        # all PyBank assignment conditions met ---------------------------------------------------------