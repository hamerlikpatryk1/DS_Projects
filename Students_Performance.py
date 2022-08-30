# %% 
#!/home/DS_Projects/Students_Performance_env/bin/activate
#source Students_Performance_env/bin/activate
# pip install -r requirements.txt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_theme()

# get data from csv file
students_data = pd.read_csv('StudentsPerformance.csv')
#print(students_data.to_string())
#print(type(students_data))

# sorting the array -> chose column/row/and sorting algorithm
grades = students_data.sort_values(by = "math score", ascending = False, kind = 'mergesort')
print(grades)

# simple filtering by column
# grades = grades.filter(items= ['math score', 'reading score', 'writing score']) 

# filtering by value #loc
# czy zrobić z tego funkcję i do każdej kolumny osobno?
good_grades = grades.loc[(grades['math score'] >= 66) &
                         (grades['reading score'] >= 66) &
                         (grades['writing score'] >= 66)]

""" STATISTIC
math_stat = grades['math score'].describe()
print(math_stat)
reading_mean = grades['reading score'].mean()
reading_median = grades['reading score'].quantile(q = 0.50)
print('Mean of the reading score = ', reading_mean, ', median = ', reading_median) """

# plotting data
sns.relplot(data=grades, x='reading score', y='math score', hue ='test preparation course')
sns.relplot(x="math score", y="reading score", data=good_grades)
sns.displot(good_grades, x="math score", hue="gender", element="step")
plt.show()

# write to csv
good_grades.to_csv('grades_data.csv', index=False)

# %%
