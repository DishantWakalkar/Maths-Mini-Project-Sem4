import csv
import random

with open('Outcomes.csv','w',newline='') as file:
    csv_write = csv.writer(file, delimiter=' ')

    noOfTrails = int(input('Enter no of trails : '))

    for i in range(0,noOfTrails):
        # csv_write.writerow(['Trail '] + [str(i + 1)])
        for i in range(1,11):
            num = random.randint(0,1)
            csv_write.writerow([num])

