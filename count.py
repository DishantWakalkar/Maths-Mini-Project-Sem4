import csv
# import panda as pd

# obj=csv.DictWriter('Outcomes.csv', fieldnames=fields)
# obj.writeheader()
# obj.writerows()
# csvfile.close()

with open('Outcomes.csv','r')as file:


    csv_read = csv.reader(file)
    i = 0
    
    for i in range(a,b):
        a = 1
        for lines in csv_read:
            if lines == ['0']:
                i=i+1
                print(lines)


            
        
    print(i)