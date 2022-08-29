#!/home/DS_Projects/Students_Performance_env/bin/activate
# source Students_Performance_venv/bin/activate
# simple fibonacci for initial commit
# pip install -r requirements.txt

# Modulo function -> check if number is even or odd
from heapq import merge
import numpy as np
import pandas as pd

# get data from csv file
students_data = pd.read_csv('StudentsPerformance.csv')
print(students_data.to_string())
print(type(students_data))

# sorting the array -> chose column/row/and sorting algorithm
grades = students_data.sort_values(by = "math score", ascending = False, kind = 'mergesort') #axis = 0, kind = 'quicksort', order = 5)
print(grades)
# write to csv
grades.to_csv('grades_data.csv', index=False)