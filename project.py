import pandas as pd
import numpy as np

"""
학생 기본정보를 column 이름으로
(Last Name,First Name,Email)

quiz 1~5 grade 4% 20
hw 1~10 (hw/max points) 5% 50
exam 1~3 (exam/max points) 10% 30

 #   Last Name      First Name      Email      Final Grade
---  ---------      ---------       ----- 
 
"""

data1 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_1_grades.csv')
data2 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_2_grades.csv')
data3= pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_3_grades.csv')
data4 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_4_grades.csv')
data5 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_5_grades.csv')
data6 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/hw_exam_grades.csv', usecols=["First Name", "Last Name", "Homework 1", "Homework 1 - Max Points", "Homework 2", "Homework 2 - Max Points", "Homework 3", "Homework 3 - Max Points", "Homework 4", "Homework 4 - Max Points", "Homework 5", "Homework 5 - Max Points", "Homework 6", "Homework 6 - Max Points", "Homework 7", "Homework 7 - Max Points", "Homework 8", "Homework 8 - Max Points", "Homework 9", "Homework 9 - Max Points", "Homework 10", "Homework 10 - Max Points", "Exam 1", "Exam 1 - Max Points", "Exam 2", "Exam 2 - Max Points", "Exam 3", "Exam 3 - Max Points"])
# print(data1.info())
# print(data2.info())
# print(data3.info())
# print(data4.info())
# print(data5.info())
# print(data6.info())
data1.rename(columns = {'Grade':'Quiz1'}, inplace = True)
data2.rename(columns = {'Grade':'Quiz2'}, inplace = True)
data3.rename(columns = {'Grade':'Quiz3'}, inplace = True)
data4.rename(columns = {'Grade':'Quiz4'}, inplace = True)
data5.rename(columns = {'Grade':'Quiz5'}, inplace = True)

data = data1.merge(data2, on=["Last Name", "First Name", "Email"])
data = data.merge(data3, on=["Last Name", "First Name", "Email"])
data = data.merge(data4, on=["Last Name", "First Name", "Email"])
data = data.merge(data5, on=["Last Name", "First Name", "Email"])
data = data.merge(data6, on=["Last Name", "First Name"], how="left")

print(data.info())

"""
, usecols=[]
"""