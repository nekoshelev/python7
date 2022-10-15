def all_contact():
 import csv
 
 with open('lesson7/homework/Phonebook.csv', newline='', encoding = 'utf-8') as File:  
     reader = csv.reader(File)
     for row in reader:
         print(row)
