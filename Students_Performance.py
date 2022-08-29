#!/home/DS_Projects/Students_Performance_env/bin/activate
# source Students_Performance_venv/bin/activate
# simple fibonacci for initial commit
# pip install -r requirements.txt

# Modulo function -> check if number is even or odd
import csv
import numpy as np

# get data from csv file
# problem with type in np csv loader made me use csv.reader
with open ('StudentsPerformance.csv', 'r') as f:
    students_data = list(csv.reader(f, delimiter=','))

students_data = np.array(students_data)
print(students_data)
print(type(students_data))

# sorting the array -> chose column/row/and sorting algorithm

#print(students_array.sort(order = 'math score')) #axis = 0, kind = 'quicksort', order = 5)

# write to csv
with open('grades_data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerows(students_data)