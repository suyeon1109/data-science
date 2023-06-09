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
data6 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/hw_exam_grades.csv')
print(data1)
# print(data2.info())
# print(data3.info())
# print(data4.info())
# print(data5.info())
# print(data6.info())