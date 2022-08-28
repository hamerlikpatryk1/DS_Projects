#!/home/DS_Projects/Students_Performance_env/bin/activate
# source Students_Performance_venv/bin/activate
# simple fibonacci for initial commit
# pip install -r requirements.txt

# Modulo function -> check if number is even or odd
import numpy as np
import pandas as pd

# get data from csv file
students_data = pd.read_csv('StudentsPerformance.csv', sep=',', header= None)
students_array = np.array(students_data)
print(students_array)

# sorting the array -> chose column/row/and sorting algorithm
sorted_grades = np.sort(students_array) #axis = 0, kind = 'quicksort', order = 5)
print(sorted_grades)
print(type(sorted_grades))

pd.DataFrame(sorted_grades).to_csv('grades_data.csv')