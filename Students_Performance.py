#!/home/DS_Projects/Students_Performance_env/bin/activate
# source Students_Performance_venv/bin/activate
# simple fibonacci for initial commit
# pip install -r requirements.txt

# Modulo function -> check if number is even or odd
import numpy as np
import pandas as pd

# get data from csv file
students_data = pd.read_csv('StudentsPerformance.csv')
print(students_data.to_string())
print(type(students_data))

# sorting the array -> chose column/row/and sorting algorithm
#print(students_data.argsort(order = 'math score')) #axis = 0, kind = 'quicksort', order = 5)

# write to csv
students_data.to_csv('grades_data.csv', index=False)