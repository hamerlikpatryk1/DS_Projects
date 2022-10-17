#!/home/DS_Projects/Students_Performance_env/bin/activate
#source Students_Performance_env/bin/activate
# pip install -r requirements.txt
from fileinput import filename
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# sns.set_theme()

# get data from csv file
class PrepareData:
    def __init__(self, name):
        print(f"Hello {name} I'm preparing data")
        self.name = name

    def preparator(self, filename):
        self.students_data = self._read_CSV(filename)
        self.grades = self._math_sort(self.students_data)
        self.good_grades = self._best_grade(self.grades)
        print(self.students_data)
        print(self.grades)
        print(self.good_grades)
        return self.students_data, self.grades, self.good_grades
    
    def _read_CSV(self, filename): 
        students_data = pd.read_csv(filename)
        return students_data

    # sorts data by mathscore
    def _math_sort(self, students_data):
        grades = students_data.sort_values(by = "math score", ascending = False, kind = 'mergesort')
        print(grades)
        return grades

    # filtering the highest scores #loc 
    def _best_grade(self, grades):
        good_grades = grades.loc[(grades['math score'] >= 66) &
                            (grades['reading score'] >= 66) &
                            (grades['writing score'] >= 66)]
        return good_grades

# bachelores with course 
def bach_with_test(grades):
    bachelor_test = grades.loc[(grades['parental level of education'] == "bachelor's degree") &
                         (grades['test preparation course'] == "completed")]
    return bachelor_test
# highschool with course    
def school_with_test(grades):
    school_test = grades.loc[(grades['parental level of education'] == "some high school") &
                         (grades['test preparation course'] == "completed")]
    return school_test

# List of course completed
def course_completed(grades):
    course = grades.loc[(grades['test preparation course'] == "completed")]
    return course
# List of course uncompleted
def course_uncompleted(grades):
    no_course = grades.loc[(grades['test preparation course'] == "none")]
    return no_course

# Grade of men with lunch 
def men_with_lunch(grades):
    men_lunch = grades.loc[(grades['gender'] == "male") &
                        (grades['lunch'] == 'standard')]
    return men_lunch
# Grade of men without lunch 
def men_without_lunch(grades):
    men_no_lunch = grades.loc[(grades['gender'] == "male") &
                        (grades['lunch'] == 'free/reduced')]
    return men_no_lunch
# Grade of women with lunch 
def women_with_lunch(grades):
    women_lunch = grades.loc[(grades['gender'] == "female")&
                        (grades['lunch'] == 'standard')]
    return women_lunch
# Grade of women without lunch 
def women_without_lunch(grades):
    women_no_lunch = grades.loc[(grades['gender'] == "female")&
                            (grades['lunch'] =='free/reduced')]
    return women_no_lunch

# mean of bachwithtest
def bach_mean(grades, score):
    bach_test_mean = bach_with_test(grades)[score].mean()
    return bach_test_mean
# mean of high schoolers
def schoolers_mean(grades, score):
    schoolers_test_mean = school_with_test(grades)[score].mean()
    return schoolers_test_mean

# mean of course completed
def course_mean(grades, score):
    course_mean = course_completed(grades)[score].mean()
    return course_mean
# mean of course uncompleted
def no_course_mean(grades, score):
    no_course_mean = course_uncompleted(grades)[score].mean()
    return no_course_mean
# median of course completed
def course_median(grades, score):
    course_mean = course_completed(grades)[score].quantile(q = 0.50)
    return course_mean
# median of course uncompleted
def no_course_median(grades, score):
    no_course_mean = course_uncompleted(grades)[score].quantile(q = 0.50)
    return no_course_mean

# mean/median of men/women with/without lunch
def men_lunch_median(grades, score):
    men_lunch = men_with_lunch(grades)[score].quantile(q = 0.50)
    return men_lunch

def men_lunchmean(grades, score):
    men_lunch = men_with_lunch(grades)[score].mean()
    return men_lunch

def men_no_lunch_median(grades, score):
    men_no_lunch = men_without_lunch(grades)[score].quantile(q = 0.50)
    return men_no_lunch

def men_no_lunch_mean(grades, score):
    men_no_lunch = men_without_lunch(grades)[score].mean()
    return men_no_lunch

def women_lunch_median(grades, score):
    woman_lunch = women_with_lunch(grades)[score].quantile(q = 0.50)
    return woman_lunch

def women_lunch_mean(grades, score):
    woman_lunch = women_with_lunch(grades)[score].mean()
    return woman_lunch

def women_no_lunch_median(grades, score):
    woman_no_lunch = women_without_lunch(grades)[score].quantile(q = 0.50)
    return woman_no_lunch

def women_no_lunch_mean(grades, score):
    woman_no_lunch = women_without_lunch(grades)[score].mean() #nie trxebas przypisywać zmiennej - od razu return -->> dać zmienne/funkcje camel case (podłoga)
    return woman_no_lunch

def main():

    prepared_data = PrepareData("Patryk")
    prepared_data.preparator('StudentsPerformance.csv')
    students_data = prepared_data.preparator(students_data)

# Main variable -> sorted grades
    grades = prepared_data.preparator(grades)

# 1 metric 
    good_grades = prepared_data.preparator(good_grades)
# 2 metric
# mean of bachelores + completed course
    print(
        '\nBachelors children math mean = ', bach_mean(grades, 'math score'),
        '\nBachelors children reading mean = ',bach_mean(grades,'reading score'),
        '\nBachelors children writing mean = ', bach_mean(grades,'writing score'))

# mean of high school + completed courses
    print(
        '\nHigh schoolers children math mean = ', schoolers_mean(grades, 'math score'), 
        '\nHigh schoolers children reading mean = ', schoolers_mean(grades,'reading score'),
        '\nHigh schoolers children writing mean = ', schoolers_mean(grades,'writing score'))

# 3 metric mean + median of course complete and uncompleted
# Mean
    print ( 
        '\nCourse completed math mean = ', course_mean(grades, 'math score'),
        '\nCourse completed reading mean =', course_mean(grades,'reading score'),
        '\nCourse completed writing mean = ', course_mean(grades,'writing score') )
    print ( 
        '\nNone course completed math mean = ', no_course_mean(grades, 'math score'),
        '\nNone course completed reading mean =', no_course_mean(grades,'reading score'),
        '\nNone course completed writing mean = ', no_course_mean(grades,'writing score') )
# Median
    print ( 
        '\nCourse completed math median = ', course_median(grades, 'math score'),
        '\nCourse completed reading median =', course_median(grades,'reading score'),
        '\nCourse completed writing median = ', course_median(grades,'writing score') )
    print ( 
        '\nNone course completed math median = ', no_course_median(grades, 'math score'),
        '\nNone course completed reading median =', no_course_median(grades,'reading score'),
        '\nNone course completed writing median = ', no_course_median(grades,'writing score') )
 
# Dodać plotting i zapisać go do pliku

# 4 metric
# Men with lunch 
    print ( 
        '\nMen with lunch math mean = ', men_lunchmean(grades, 'math score'),
        '\nMen with lunch reading mean =', men_lunchmean(grades,'reading score'),
        '\nMen with lunch writing mean = ', men_lunchmean(grades,'writing score'),
        '\nMen with lunch math median = ', men_lunch_median(grades, 'math score'),
        '\nMen with lunch reading median =', men_lunch_median(grades,'reading score'),
        '\nMen with lunch writing median = ', men_lunch_median(grades,'writing score'))
# Woman with lunch 
    print ( 
        '\nWomen with lunch math mean = ', women_lunch_mean(grades, 'math score'),
        '\nWomen with lunch reading mean =', women_lunch_mean(grades,'reading score'),
        '\nWomen with lunch writing mean = ', women_lunch_mean(grades,'writing score'),
        '\nWomen with lunch math median = ', women_lunch_median(grades, 'math score'),
        '\nWomen with lunch reading median =', women_lunch_median(grades,'reading score'),
        '\nWomen with lunch writing median = ', women_lunch_median(grades,'writing score'))
# Men without lunch
    print ( 
        '\nMen without lunch math mean = ', men_no_lunch_mean(grades, 'math score'),
        '\nMen without lunch reading mean =', men_no_lunch_mean(grades,'reading score'),
        '\nMen without lunch writing mean = ', men_no_lunch_mean(grades,'writing score'),
        '\nMen without lunch math median = ', men_no_lunch_median(grades, 'math score'),
        '\nMen without lunch reading median =', men_no_lunch_median(grades,'reading score'),
        '\nMen without lunch writing median = ', men_no_lunch_median(grades,'writing score'))
# Woman without lunch
    print ( 
        '\nWomen without lunch math mean = ', women_no_lunch_mean(grades, 'math score'),
        '\nWomen without lunch reading mean =', women_no_lunch_mean(grades,'reading score'),
        '\nWomen without lunch writing mean = ', women_no_lunch_mean(grades,'writing score'),
        '\nWomen without lunch math median = ', women_no_lunch_median(grades, 'math score'),
        '\nWomen without lunch reading median =', women_no_lunch_median(grades,'reading score'),
        '\nWomen without lunch writing median = ', women_no_lunch_median(grades,'writing score'))

# plotting data
# sns.relplot(data=grades, x='reading score', y='math score', hue ='test preparation course')
# sns.relplot(x="math score", y="reading score", data=good_grades)
# sns.displot(good_grades, x="math score", hue="gender", element="step")
# plt.show()

# write to csv
    good_grades.to_csv('grades_data.csv', index=False)
    bach_with_test(grades).to_csv('bach_grades.csv', index=False)


if __name__ == "__main__":
    main()