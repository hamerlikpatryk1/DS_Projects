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

# Grade of men with lunch 
def menwithlunch(grades):
    menlunch = grades.loc[(grades['gender'] == "male") &
                        (grades['lunch'] == 'standard')]
    return menlunch
# Grade of men without lunch 
def menwithoutlunch(grades):
    mennolunch = grades.loc[(grades['gender'] == "male") &
                        (grades['lunch'] == 'free/reduced')]
    return mennolunch
# Grade of women with lunch 
def womenwithlunch(grades):
    womenlunch = grades.loc[(grades['gender'] == "female")&
                        (grades['lunch'] == 'standard')]
    return womenlunch
# Grade of women without lunch 
def womenwithoutlunch(grades):
    womennolunch = grades.loc[(grades['gender'] == "female")&
                            (grades['lunch'] =='free/reduced')]
    return womennolunch

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

# mean/median of men/women with/without lunch
def menlunchmedian(grades, score):
    menlunch = menwithlunch(grades)[score].quantile(q = 0.50)
    return menlunch

def menlunchmean(grades, score):
    menlunch = menwithlunch(grades)[score].mean()
    return menlunch

def mennolunchmedian(grades, score):
    mennolunch = menwithoutlunch(grades)[score].quantile(q = 0.50)
    return mennolunch

def mennolunchmean(grades, score):
    mennolunch = menwithoutlunch(grades)[score].mean()
    return mennolunch

def womenlunchmedian(grades, score):
    womanlunch = womenwithlunch(grades)[score].quantile(q = 0.50)
    return womanlunch

def womenlunchmean(grades, score):
    womanlunch = womenwithlunch(grades)[score].mean()
    return womanlunch

def womennolunchmedian(grades, score):
    womannolunch = womenwithoutlunch(grades)[score].quantile(q = 0.50)
    return womannolunch

def womennolunchmean(grades, score):
    womannolunch = womenwithoutlunch(grades)[score].mean()
    return womannolunch

students_data = readCSV('StudentsPerformance.csv')

# Main variable -> sorted grades
grades = mathsort(students_data)

# 1 metric 
good_grades = bestgrade(grades)

# 2 metric
# mean of bachelores + completed course
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
# Median
print ( 
    '\nCourse completed math median = ', coursemedian(grades, 'math score'),
    '\nCourse completed reading median =', coursemedian(grades,'reading score'),
    '\nCourse completed writing median = ', coursemedian(grades,'writing score') )
print ( 
    '\nNone course completed math median = ', nocoursemedian(grades, 'math score'),
    '\nNone course completed reading median =', nocoursemedian(grades,'reading score'),
    '\nNone course completed writing median = ', nocoursemedian(grades,'writing score') )
 
# Dodać plotting i zapisać go do pliku

# 4 metric
# Men with lunch 
print ( 
    '\nMen with lunch math mean = ', menlunchmean(grades, 'math score'),
    '\nMen with lunch reading mean =', menlunchmean(grades,'reading score'),
    '\nMen with lunch writing mean = ', menlunchmean(grades,'writing score'),
    '\nMen with lunch math median = ', menlunchmedian(grades, 'math score'),
    '\nMen with lunch reading median =', menlunchmedian(grades,'reading score'),
    '\nMen with lunch writing median = ', menlunchmedian(grades,'writing score'))
# Woman With lunch 
print ( 
    '\nWomen with lunch math mean = ', womenlunchmean(grades, 'math score'),
    '\nWomen with lunch reading mean =', womenlunchmean(grades,'reading score'),
    '\nWomen with lunch writing mean = ', womenlunchmean(grades,'writing score'),
    '\nWomen with lunch math median = ', womenlunchmedian(grades, 'math score'),
    '\nWomen with lunch reading median =', womenlunchmedian(grades,'reading score'),
    '\nWomen with lunch writing median = ', womenlunchmedian(grades,'writing score'))
# Men without lunch
print ( 
    '\nMen with lunch math mean = ', mennolunchmean(grades, 'math score'),
    '\nMen with lunch reading mean =', mennolunchmean(grades,'reading score'),
    '\nMen with lunch writing mean = ', mennolunchmean(grades,'writing score'),
    '\nMen with lunch math median = ', mennolunchmedian(grades, 'math score'),
    '\nMen with lunch reading median =', mennolunchmedian(grades,'reading score'),
    '\nMen with lunch writing median = ', mennolunchmedian(grades,'writing score'))
# Woman without lunch
print ( 
    '\nWomen with lunch math mean = ', womennolunchmean(grades, 'math score'),
    '\nWomen with lunch reading mean =', womennolunchmean(grades,'reading score'),
    '\nWomen with lunch writing mean = ', womennolunchmean(grades,'writing score'),
    '\nWomen with lunch math median = ', womennolunchmedian(grades, 'math score'),
    '\nWomen with lunch reading median =', womennolunchmedian(grades,'reading score'),
    '\nWomen with lunch writing median = ', womennolunchmedian(grades,'writing score'))
    
# 4 metryki -> 1 best grades, 2 mean of bachelores with test complete -> compare with high school and completed coures , 
# 3 mean + median of test complete and uncompleted, 4 mean + median of males/females with standard lunch + without lunch 

# plotting data
# sns.relplot(data=grades, x='reading score', y='math score', hue ='test preparation course')
# sns.relplot(x="math score", y="reading score", data=good_grades)
# sns.displot(good_grades, x="math score", hue="gender", element="step")
# plt.show()

# write to csv
good_grades.to_csv('grades_data.csv', index=False)
bachwithtest(grades).to_csv('bach_grades.csv', index=False)