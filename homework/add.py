def add():
 from os.path import exists
 from CSV_creating import creating
 from File_writing import writing_scv
 from File_writing import writing_txt


 path = 'lesson7/homework/Phonebook.csv'
 valid = exists(path)
 if not valid:
    creating()

 writing_scv()
 writing_txt()