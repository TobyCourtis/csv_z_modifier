import csv
from time import sleep

def add_Z_placement(overwrite, inputFile, outputFile):
    with open(inputFile + '.csv','r') as csvinput:
        with open('./' + outputFile + '.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            
            all = []
            row = next(reader)
            if(float(row[1]) < 5000):
                lengthX = length1
            elif (5000 < float(row[1]) < 8000):
                lengthX = length2
            elif (9000 < float(row[1]) < 14000):
                lengthX = length3
            elif (15000 < float(row[1])):
                lengthX = length4
            else:
                print("X position out of bounds")
        
            if (overwrite):
                row[12] = lengthX
            else:
                row.append(lengthX)
            all.append(row)

            for row in reader:
                if(float(row[1]) < 5000):
                    lengthX = length1
                elif (5000 < float(row[1]) < 8000):
                    lengthX = length2
                elif (9000 < float(row[1]) < 14000):
                    lengthX = length3
                elif (15000 < float(row[1])):
                    lengthX = length4
                else:
                    print("X position out of bounds")
                    break
                if (overwrite):
                    row[12] = lengthX
                else:
                    row.append(lengthX)
                all.append(row)

            writer.writerows(all)
    print("CSV saved successfully as " + outputFile + ".csv")
            
print("Reading in CSV")

fileIn = input("\nPlease input filename for alteration: ")
fileOut = input("\nPlease give output filename: ")

#read in Length shit
length1 = input("\nPlease input Z placement for length 1: ")
length2 = input("Please input Z placement for length 2: ")
length3 = input("Please input Z placement for length 3: ")
length4 = input("Please input Z placement for length 4: ")

overwrite = False
print("\nYou have input Z positions as length 1: {}mm, length 2: {}mm, length 3: {}mm and length 4: {}mm".format(length1,length2,length3,length4))
confirmation = input("Press Y to add Z positions [Y/n]: ")
if (confirmation == "Y"):
    with open(fileIn + '.csv','r') as check:
        reader = csv.reader(check)
        row = next(reader)
        try:
            temp = row[12]
            overwrite = True
        except:
            overwrite = False
        if (overwrite):
            confirmation2 = input("Z placements already exist, would you like to replace them? [Y/n]: ")
            if(confirmation2 == "Y"):
                add_Z_placement(overwrite, fileIn, fileOut)
                sleep(2)
            else:
                print("Exited without changing Z positions")
                sleep(2)
        else:
            add_Z_placement(overwrite, fileIn, fileOut)
            sleep(2)
else:
    print("Exiting application")
