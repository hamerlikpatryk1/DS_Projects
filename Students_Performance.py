#!/home/DS_Projects/Students_Performance_env/bin/activate
#source Students_Performance_env/bin/activate
# pip install -r requirements.txt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# sns.set_theme()

# get data from csv file
def readCSV(filename):
    students_data = pd.read_csv(filename)
    return students_data

# sorts data by mathscore
def mathsort(students_data):
    grades = students_data.sort_values(by = "math score", ascending = False, kind = 'mergesort')
    print(grades)
    return grades

# filtering the highest scores #loc 
def bestgrade(grades):
    good_grades = grades.loc[(grades['math score'] >= 66) &
                         (grades['reading score'] >= 66) &
                         (grades['writing score'] >= 66)]
    return good_grades

# bachelores with course 
def bachwithtest(grades):
    bachelortest = grades.loc[(grades['parental level of education'] == "bachelor's degree") &
                         (grades['test preparation course'] == "completed")]
    return bachelortest
# highschool with course    
def schoolwithtest(grades):
    schooltest = grades.loc[(grades['parental level of education'] == "some high school") &
                         (grades['test preparation course'] == "completed")]
    return schooltest

# List of course completed
def coursecompleted(grades):
    course = grades.loc[(grades['test preparation course'] == "completed")]
    return course
# List of course uncompleted
def courseuncompleted(grades):
    nocourse = grades.loc[(grades['test preparation course'] == "none")]
    return nocourse

# mean of bachwithtest
def bachmean(grades, score):
    bachtestmean = bachwithtest(grades)[score].mean()
    return bachtestmean
# mean of high schoolers
def schoolersmean(grades, score):
    schoolerstestmean = schoolwithtest(grades)[score].mean()
    return schoolerstestmean

# mean of course completed
def coursemean(grades, score):
    coursemean = coursecompleted(grades)[score].mean()
    return coursemean
# mean of course uncompleted
def nocoursemean(grades, score):
    nocoursemean = courseuncompleted(grades)[score].mean()
    return nocoursemean
# median of course completed
def coursemedian(grades, score):
    coursemean = coursecompleted(grades)[score].quantile(q = 0.50)
    return coursemean
# median of course uncompleted
def nocoursemedian(grades, score):
    nocoursemean = courseuncompleted(grades)[score].quantile(q = 0.50)
    return nocoursemean
students_data = readCSV('StudentsPerformance.csv')

# Main variable -> sorted grades
grades = mathsort(students_data)

# 1 metric 
good_grades = bestgrade(grades)

#2 metric -> mean of bachelores + completed course
print(
    '\nBachelors children math mean = ', bachmean(grades, 'math score'),
    '\nBachelors children reading mean = ',bachmean(grades,'reading score'),
    '\nBachelors children writing mean = ', bachmean(grades,'writing score'))

# mean of high school + completed courses
print(
    '\nHigh schoolers children math mean = ', schoolersmean(grades, 'math score'), 
    '\nHigh schoolers children reading mean = ', schoolersmean(grades,'reading score'),
    '\nHigh schoolers children writing mean = ', schoolersmean(grades,'writing score'))

# 3 metric mean + median of course complete and uncompleted
# Mean
print ( 
    '\nCourse completed math mean = ', coursemean(grades, 'math score'),
    '\nCourse completed reading mean =', coursemean(grades,'reading score'),
    '\nCourse completed writing mean = ', coursemean(grades,'writing score') )
print ( 
    '\nNone course completed math mean = ', nocoursemean(grades, 'math score'),
    '\nNone course completed reading mean =', nocoursemean(grades,'reading score'),
    '\nNone course completed writing mean = ', nocoursemean(grades,'writing score') )
#Median
print ( 
    '\nCourse completed math median = ', coursemedian(grades, 'math score'),
    '\nCourse completed reading median =', coursemedian(grades,'reading score'),
    '\nCourse completed writing median = ', coursemedian(grades,'writing score') )
print ( 
    '\nNone course completed math median = ', nocoursemedian(grades, 'math score'),
    '\nNone course completed reading median =', nocoursemedian(grades,'reading score'),
    '\nNone course completed writing median = ', nocoursemedian(grades,'writing score') )

# 4 metryki -> 1 best grades, 2 mean of bachelores with test complete -> compare with high school and completed coures , 3 mean + median of test complete and uncompleted, 4 mean + median of males/females with standard lunch 
#   
# STATISTIC
# math_stat = grades['math score'].describe()
# print(math_stat)
# reading_mean = grades['reading score'].mean()
# reading_median = grades['reading score'].quantile(q = 0.50)
# print('Mean of the reading score = ', reading_mean, ', median = ', reading_median) """

# plotting data
# sns.relplot(data=grades, x='reading score', y='math score', hue ='test preparation course')
# sns.relplot(x="math score", y="reading score", data=good_grades)
# sns.displot(good_grades, x="math score", hue="gender", element="step")
# plt.show()

# write to csv
good_grades.to_csv('grades_data.csv', index=False)
bachwithtest(grades).to_csv('bach_grades.csv', index=False)