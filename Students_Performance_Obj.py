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
        students_data = self._read_CSV(filename)
        grades = self._math_sort(students_data)
        good_grades = self._best_grade(grades)
        print(students_data)
        print(grades)
        print(good_grades)
        return students_data, grades, good_grades
    
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

class EducationWithCourse:
    def __init__(self):
        print(f"\nNOW I'LL SHOW RESULTS BASED CURSE DONE AND LEVEL OF PARENTAL EDUCATION")

    def participants_with_test(self, grades, score):
        bachelor_test = self._bach_with_test(grades)
        school_test = self._school_with_test(grades)
        bach_test_mean = self._bach_mean(bachelor_test, score)
        schoolers_test_mean = self._schoolers_mean(school_test, score)
        return bachelor_test, school_test, bach_test_mean, schoolers_test_mean 

    # bachelores with course 
    def _bach_with_test(self, grades):
        bachelor_test = grades.loc[(grades['parental level of education'] == "bachelor's degree") &
                            (grades['test preparation course'] == "completed")]
        return bachelor_test

    # highschool with course    
    def _school_with_test(self, grades):
        school_test = grades.loc[(grades['parental level of education'] == "some high school") &
                            (grades['test preparation course'] == "completed")]
        return school_test

    # mean of bachwithtest
    def _bach_mean(self, bachelor_test, score):
        bach_test_mean = bachelor_test[score].mean()
        return bach_test_mean

    # mean of high schoolers
    def _schoolers_mean(self, school_test, score):
        schoolers_test_mean = school_test[score].mean()
        return schoolers_test_mean

class CourseCompletedUncompleted:
    def __init__(self):
        print(f"\nNOW I'LL SHOW RESULTS BASED ON COURSE: ")

    def course_impact(self, grades, score):
        course_completed = self._course_completed(grades)
        course_uncompleted = self._course_uncompleted(grades)
        course_mean = self._course_mean(course_completed, score)
        no_course_mean = self._no_course_mean(course_uncompleted, score)
        course_median = self._course_median(course_completed, score)
        no_course_median = self._no_course_median(course_uncompleted, score)
        return course_completed, course_uncompleted, course_mean, no_course_mean, course_median, no_course_median
    # List of course completed
    def _course_completed(self, grades):
        course_completed = grades.loc[(grades['test preparation course'] == "completed")]
        return course_completed
    # List of course uncompleted
    def _course_uncompleted(self, grades):
        course_uncompleted = grades.loc[(grades['test preparation course'] == "none")]
        return course_uncompleted
    # mean of course completed
    def _course_mean(self, course_completed, score):
        course_mean = course_completed[score].mean()
        return course_mean
    # mean of course uncompleted
    def _no_course_mean(self, course_uncompleted, score):
        no_course_mean = course_uncompleted[score].mean()
        return no_course_mean
    # median of course completed
    def _course_median(self, course_completed, score):
        course_median = course_completed[score].quantile(q = 0.50)
        return course_median
    # median of course uncompleted
    def _no_course_median(self, course_uncompleted, score):
        no_course_median = course_uncompleted[score].quantile(q = 0.50)
        return no_course_median

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
    students_data = prepared_data.preparator('StudentsPerformance.csv')[0]
    print(students_data)
# Main variable -> sorted grades
    grades = prepared_data.preparator('StudentsPerformance.csv')[1]
# 1 metric 
    good_grades = prepared_data.preparator('StudentsPerformance.csv')[2]
    print(good_grades)

# 2 metric
    mean_data = EducationWithCourse()
    bach_mean_math = mean_data.participants_with_test(grades, 'math score')[2]
    bach_mean_read = mean_data.participants_with_test(grades, 'reading score')[2]
    bach_mean_write = mean_data.participants_with_test(grades, 'writing score')[2]
    highschooler_mean_math = mean_data.participants_with_test(grades, 'math score')[3]
    highschooler_mean_read = mean_data.participants_with_test(grades, 'reading score')[3]
    highschooler_mean_write = mean_data.participants_with_test(grades, 'writing score')[3]
    bach_math = mean_data.participants_with_test(grades, 'math score')[0]
    bach_read = mean_data.participants_with_test(grades, 'reading score')[0]
    bach_write = mean_data.participants_with_test(grades, 'writing score')[0]
    all_participants_with_test = bach_math.append([bach_read,bach_write])
    # mean of bachelores + completed course
    print(
        '\nBachelors children math mean = ', bach_mean_math,
        '\nBachelors children reading mean = ',bach_mean_read,
        '\nBachelors children writing mean = ', bach_mean_write)

    # mean of high school + completed courses
    print(
        '\nHigh schoolers children math mean = ', highschooler_mean_math, 
        '\nHigh schoolers children reading mean = ', highschooler_mean_read,
        '\nHigh schoolers children writing mean = ', highschooler_mean_write)

# 3 metric mean + median of course complete and uncompleted
    results_course_related = CourseCompletedUncompleted()
# Mean
#I'll try other convention - full name in print (no variable)
    print ( 
        '\nCourse completed math mean = ', results_course_related.course_impact(grades, 'math score')[2],
        '\nCourse completed reading mean =', results_course_related.course_impact(grades,'reading score')[2],
        '\nCourse completed writing mean = ', results_course_related.course_impact(grades,'writing score')[2] )
    print ( 
        '\nNone course completed math mean = ', results_course_related.course_impact(grades, 'math score')[3],
        '\nNone course completed reading mean =', results_course_related.course_impact(grades,'reading score')[3],
        '\nNone course completed writing mean = ', results_course_related.course_impact(grades,'writing score')[3] )
# Median
    print ( 
        '\nCourse completed math median = ', results_course_related.course_impact(grades, 'math score')[4],
        '\nCourse completed reading median =', results_course_related.course_impact(grades,'reading score')[4],
        '\nCourse completed writing median = ', results_course_related.course_impact(grades,'writing score')[4] )
    print ( 
        '\nNone course completed math median = ', results_course_related.course_impact(grades, 'math score')[5],
        '\nNone course completed reading median =', results_course_related.course_impact(grades,'reading score')[5],
        '\nNone course completed writing median = ', results_course_related.course_impact(grades,'writing score')[5] )
 
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
    all_participants_with_test.to_csv('bach_grades.csv', index=False)


if __name__ == "__main__":
    main()