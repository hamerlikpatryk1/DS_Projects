#!/home/DS_Projects/Students_Performance_env/bin/activate
#source Students_Performance_env/bin/activate
# pip install -r requirements.txt
from fileinput import filename
import pandas as pd


# get data from csv file
class PrepareData:
    def __init__(self, name):
        print(f"Hello {name} I'm preparing data")
        self.name = name

    def preparator(self, filename):
        preparator_dict = dict()
        preparator_dict['students_data'] = self._read_CSV(filename)
        preparator_dict['grades'] = self._students_data(preparator_dict['students_data'])
        preparator_dict['good_grades'] = self._good_grades(preparator_dict['grades'] )
        print(preparator_dict['students_data'])
        print(preparator_dict['grades'])
        print(preparator_dict['good_grades'])
        return preparator_dict
    
    def _read_CSV(self, filename): 
        return pd.read_csv(filename)

    # sorts data by mathscore
    def _students_data(self, students_data):
        return students_data.sort_values(by = "math score", ascending = False, kind = 'mergesort')

    # filtering the highest scores #loc 
    def _good_grades(self, grades):
        return grades.loc[(grades['math score'] >= 66) &
                            (grades['reading score'] >= 66) &
                            (grades['writing score'] >= 66)]
        

class EducationWithCourse:
    def __init__(self):
        print(f"\nNOW I'LL SHOW RESULTS BASED CURSE DONE AND LEVEL OF PARENTAL EDUCATION")

    def participants_with_test(self, grades, score):
        participants_test_dict = dict()
        participants_test_dict['bachelor_test'] = self._bach_with_test(grades)
        participants_test_dict['school_test'] = self._school_with_test(grades)
        participants_test_dict['bach_test_mean'] = self._bach_mean(participants_test_dict['bachelor_test'], score)
        participants_test_dict['schoolers_test_mean'] = self._schoolers_mean(participants_test_dict['school_test'] , score)
        return participants_test_dict
    # bachelores with course 
    def _bach_with_test(self, grades):
        return grades.loc[(grades['parental level of education'] == "bachelor's degree") &
                            (grades['test preparation course'] == "completed")]
        
    # highschool with course    
    def _school_with_test(self, grades):
        return grades.loc[(grades['parental level of education'] == "some high school") &
                            (grades['test preparation course'] == "completed")]
         
    # mean of bachwithtest
    def _bach_mean(self, bachelor_test, score):
        return bachelor_test[score].mean()
         
    # mean of high schoolers
    def _schoolers_mean(self, school_test, score):
        return school_test[score].mean()
         

class CourseCompletedUncompleted:
    def __init__(self):
        print(f"\nNOW I'LL SHOW RESULTS BASED ON COURSE: ")

    def course_impact(self, grades, score):
        course_impact_dict = dict()
        course_impact_dict['course_completed'] = self._course_completed(grades)
        course_impact_dict['course_uncompleted'] = self._course_uncompleted(grades)
        course_impact_dict['course_mean'] = self._course_mean(course_impact_dict['course_completed'], score)
        course_impact_dict ['no_course_mean'] = self._no_course_mean(course_impact_dict['course_uncompleted'], score)
        course_impact_dict ['course_median'] = self._course_median(course_impact_dict['course_completed'], score)
        course_impact_dict ['no_course_median'] = self._no_course_median(course_impact_dict['course_uncompleted'], score)
        return course_impact_dict

    # List of course completed
    def _course_completed(self, grades):
        return grades.loc[(grades['test preparation course'] == "completed")]
         
    # List of course uncompleted
    def _course_uncompleted(self, grades):
        return grades.loc[(grades['test preparation course'] == "none")]
         
    # mean of course completed
    def _course_mean(self, course_completed, score):
        return course_completed[score].mean()
         
    # mean of course uncompleted
    def _no_course_mean(self, course_uncompleted, score):
        return course_uncompleted[score].mean()
    
    # median of course completed
    def _course_median(self, course_completed, score):
        return course_completed[score].quantile(q = 0.50)
        
    # median of course uncompleted
    def _no_course_median(self, course_uncompleted, score):
        return course_uncompleted[score].quantile(q = 0.50)


class LunchAndGender:
    def __init__(self):
        print(f"\nNOW I'LL SHOW RESULTS BASED ON LUNCH AND GENDER: ")

    def lunch_gender_impact(self, grades, score):
        lunch_gender_dict = dict()
        lunch_gender_dict['men_with_lunch'] = self._men_with_lunch(grades)
        lunch_gender_dict['men_no_lunch'] = self._men_without_lunch(grades)
        lunch_gender_dict['women_lunch'] = self._women_with_lunch(grades)
        lunch_gender_dict['women_no_lunch'] = self._women_without_lunch(grades)

        lunch_gender_dict['men_lunch_median'] = self._men_lunch_median(lunch_gender_dict['men_with_lunch'], grades, score)
        lunch_gender_dict['men_lunch_mean'] = self._men_lunch_mean(lunch_gender_dict['men_with_lunch'], grades, score)
        lunch_gender_dict['men_no_lunch_median'] = self._men_no_lunch_median(lunch_gender_dict['men_no_lunch'] , grades, score)
        lunch_gender_dict['men_no_lunch_mean']= self._men_no_lunch_mean(lunch_gender_dict['men_no_lunch'] , grades, score)
        
        lunch_gender_dict['women_lunch_median'] = self._women_lunch_median(lunch_gender_dict['women_lunch'], grades, score)
        lunch_gender_dict['women_lunch_mean'] = self._women_lunch_mean(lunch_gender_dict['women_lunch'], grades, score)
        lunch_gender_dict['women_no_lunch_median'] = self._women_no_lunch_median(lunch_gender_dict['women_no_lunch'], grades, score)
        lunch_gender_dict['women_no_lunch_mean'] = self._women_no_lunch_mean(lunch_gender_dict['women_no_lunch'], grades, score)
        
        return lunch_gender_dict

    # List of course completed
    # Grade of men with lunch 
    def _men_with_lunch(self, grades):
        return grades.loc[(grades['gender'] == "male") &
                            (grades['lunch'] == 'standard')]
         
    # Grade of men without lunch 
    def _men_without_lunch(self, grades):
        return grades.loc[(grades['gender'] == "male") &
                            (grades['lunch'] == 'free/reduced')]

    # Grade of women with lunch 
    def _women_with_lunch(self, grades):
        return grades.loc[(grades['gender'] == "female")&
                            (grades['lunch'] == 'standard')]

    # Grade of women without lunch 
    def _women_without_lunch(self, grades):
        return grades.loc[(grades['gender'] == "female")&
                                (grades['lunch'] =='free/reduced')]

    # mean/median of men/women with/without lunch
    def _men_lunch_median(self, men_with_lunch, grades, score):
        return men_with_lunch[score].quantile(q = 0.50)

    def _men_lunch_mean(self, men_with_lunch, grades, score):
        return men_with_lunch[score].mean()

    def _men_no_lunch_median(self, men_without_lunch, grades, score):
        return men_without_lunch[score].quantile(q = 0.50)

    def _men_no_lunch_mean(self, men_without_lunch, grades, score):
        return men_without_lunch[score].mean()

    def _women_lunch_median(self, women_with_lunch, grades, score):
        return women_with_lunch[score].quantile(q = 0.50)

    def _women_lunch_mean(self, women_with_lunch, grades, score):
        return women_with_lunch[score].mean()

    def _women_no_lunch_median(self, women_without_lunch, grades, score):
        return women_without_lunch[score].quantile(q = 0.50)

    def _women_no_lunch_mean(self, women_without_lunch, grades, score):
        return women_without_lunch[score].mean()


def main():

    prepared_data = PrepareData("Patryk")
    students_data = prepared_data.preparator('StudentsPerformance.csv')['students_data']
    print(students_data)
    grades = prepared_data.preparator('StudentsPerformance.csv')['grades']
# 1 metric 
    good_grades = prepared_data.preparator('StudentsPerformance.csv')['good_grades']
    print(good_grades)

# 2 metric
    mean_data = EducationWithCourse()
    bach_mean_math = mean_data.participants_with_test(grades, 'math score')['bach_test_mean']
    bach_mean_read = mean_data.participants_with_test(grades, 'reading score')['bach_test_mean']
    bach_mean_write = mean_data.participants_with_test(grades, 'writing score')['bach_test_mean']
    highschooler_mean_math = mean_data.participants_with_test(grades, 'math score')['schoolers_test_mean'] 
    highschooler_mean_read = mean_data.participants_with_test(grades, 'reading score')['schoolers_test_mean'] 
    highschooler_mean_write = mean_data.participants_with_test(grades, 'writing score')['schoolers_test_mean'] 
    bach_math = mean_data.participants_with_test(grades, 'math score')['bachelor_test']
    bach_read = mean_data.participants_with_test(grades, 'reading score')['bachelor_test']
    bach_write = mean_data.participants_with_test(grades, 'writing score')['bachelor_test']
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
        '\nCourse completed math mean = ', results_course_related.course_impact(grades, 'math score')['course_mean'],
        '\nCourse completed reading mean =', results_course_related.course_impact(grades,'reading score')['course_mean'],
        '\nCourse completed writing mean = ', results_course_related.course_impact(grades,'writing score')['course_mean'] )
    print ( 
        '\nNone course completed math mean = ', results_course_related.course_impact(grades, 'math score')['no_course_mean'],
        '\nNone course completed reading mean =', results_course_related.course_impact(grades,'reading score')['no_course_mean'],
        '\nNone course completed writing mean = ', results_course_related.course_impact(grades,'writing score')['no_course_mean'] )
# Median
    print ( 
        '\nCourse completed math median = ', results_course_related.course_impact(grades, 'math score')['course_median'],
        '\nCourse completed reading median =', results_course_related.course_impact(grades,'reading score')['course_median'],
        '\nCourse completed writing median = ', results_course_related.course_impact(grades,'writing score')['course_median'] )
    print ( 
        '\nNone course completed math median = ', results_course_related.course_impact(grades, 'math score')['no_course_median'],
        '\nNone course completed reading median =', results_course_related.course_impact(grades,'reading score')['no_course_median'],
        '\nNone course completed writing median = ', results_course_related.course_impact(grades,'writing score')['no_course_median'] )
 
# Dodać plotting i zapisać go do pliku
# 4 metric
    results_lunch_gender_related = LunchAndGender()
# Men with lunch 
    print ( 
        '\nMen with lunch math mean = ', results_lunch_gender_related.lunch_gender_impact(grades, 'math score')['men_lunch_mean'],
        '\nMen with lunch reading mean =', results_lunch_gender_related.lunch_gender_impact(grades,'reading score')['men_lunch_mean'],
        '\nMen with lunch writing mean = ', results_lunch_gender_related.lunch_gender_impact(grades,'writing score')['men_lunch_mean'],
        '\nMen with lunch math median = ', results_lunch_gender_related.lunch_gender_impact(grades, 'math score')['men_lunch_median'],
        '\nMen with lunch reading median =', results_lunch_gender_related.lunch_gender_impact(grades,'reading score')['men_lunch_median'],
        '\nMen with lunch writing median = ', results_lunch_gender_related.lunch_gender_impact(grades,'writing score')['men_lunch_median'])
# Woman with lunch 
    print ( 
        '\nWomen with lunch math mean = ', results_lunch_gender_related.lunch_gender_impact(grades, 'math score')['women_lunch_mean'],
        '\nWomen with lunch reading mean =', results_lunch_gender_related.lunch_gender_impact(grades,'reading score')['women_lunch_mean'],
        '\nWomen with lunch writing mean = ', results_lunch_gender_related.lunch_gender_impact(grades,'writing score')['women_lunch_mean'],
        '\nWomen with lunch math median = ', results_lunch_gender_related.lunch_gender_impact(grades, 'math score')['women_lunch_median'],
        '\nWomen with lunch reading median =', results_lunch_gender_related.lunch_gender_impact(grades,'reading score')['women_lunch_median'],
        '\nWomen with lunch writing median = ', results_lunch_gender_related.lunch_gender_impact(grades,'writing score')['women_lunch_median'])
# Men without lunch
    print ( 
        '\nMen without lunch math mean = ', results_lunch_gender_related.lunch_gender_impact(grades, 'math score')['men_no_lunch_mean'],
        '\nMen without lunch reading mean =', results_lunch_gender_related.lunch_gender_impact(grades,'reading score')['men_no_lunch_mean'],
        '\nMen without lunch writing mean = ', results_lunch_gender_related.lunch_gender_impact(grades,'writing score')['men_no_lunch_mean'],
        '\nMen without lunch math median = ', results_lunch_gender_related.lunch_gender_impact(grades, 'math score')['men_no_lunch_median'],
        '\nMen without lunch reading median =', results_lunch_gender_related.lunch_gender_impact(grades,'reading score')['men_no_lunch_median'],
        '\nMen without lunch writing median = ', results_lunch_gender_related.lunch_gender_impact(grades,'writing score')['men_no_lunch_median'])
# Woman without lunch
    print ( 
        '\nWomen without lunch math mean = ', results_lunch_gender_related.lunch_gender_impact(grades, 'math score')['women_no_lunch_mean'],
        '\nWomen without lunch reading mean =', results_lunch_gender_related.lunch_gender_impact(grades,'reading score')['women_no_lunch_mean'],
        '\nWomen without lunch writing mean = ', results_lunch_gender_related.lunch_gender_impact(grades,'writing score')['women_no_lunch_mean'],
        '\nWomen without lunch math median = ', results_lunch_gender_related.lunch_gender_impact(grades, 'math score')['women_no_lunch_median'],
        '\nWomen without lunch reading median =', results_lunch_gender_related.lunch_gender_impact(grades,'reading score')['women_no_lunch_median'],
        '\nWomen without lunch writing median = ', results_lunch_gender_related.lunch_gender_impact(grades,'writing score')['women_no_lunch_median'])

# write to csv
    good_grades.to_csv('grades_data.csv', index=False)
    all_participants_with_test.to_csv('bach_grades.csv', index=False)


if __name__ == "__main__":
    main()