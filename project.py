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

# data1 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_1_grades.csv')
# data2 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_2_grades.csv')
# data3= pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_3_grades.csv')
# data4 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_4_grades.csv')
# data5 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_5_grades.csv')
# data6 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/hw_exam_grades.csv', usecols=["First Name", "Last Name", "Homework 1"])
# # , "Homework 1 - Max Points", "Homework 2", "Homework 2 - Max Points", "Homework 3", "Homework 3 - Max Points", "Homework 4", "Homework 4 - Max Points", "Homework 5", "Homework 5 - Max Points", "Homework 6", "Homework 6 - Max Points", "Homework 7", "Homework 7 - Max Points", "Homework 8", "Homework 8 - Max Points", "Homework 9", "Homework 9 - Max Points", "Homework 10", "Homework 10 - Max Points", "Exam 1", "Exam 1 - Max Points", "Exam 2", "Exam 2 - Max Points", "Exam 3", "Exam 3 - Max Points"])
# # print(data1.info())
# # print(data2.info())
# # print(data3.info())
# # print(data4.info())
# # print(data5.info())
# # print(data6.info())

# data1.rename(columns = {'Grade':'Quiz1'}, inplace = True)
# data2.rename(columns = {'Grade':'Quiz2'}, inplace = True)
# data3.rename(columns = {'Grade':'Quiz3'}, inplace = True)
# data4.rename(columns = {'Grade':'Quiz4'}, inplace = True)
# data5.rename(columns = {'Grade':'Quiz5'}, inplace = True)
# data6.fillna(0,inplace=True)
# # print(data6.info())

# # print(data6.to_string())
# data = data1.merge(data2, on=["Last Name", "First Name", "Email"])
# data = data.merge(data3, on=["Last Name", "First Name", "Email"])
# data = data.merge(data4, on=["Last Name", "First Name", "Email"])
# data = data.merge(data5, on=["Last Name", "First Name", "Email"])
# data = data.merge(data6, on=["Last Name", "First Name"], how="outer")

# print(data.to_string())

"""
, usecols=[]
"""



roster = pd.read_csv(
    "data-science/data/roster.csv",
    converters={"NetID": str.lower, "Email Address": str.lower},
    usecols=["Section", "Email Address", "NetID"],
    index_col="NetID",
)

hw_exam_grades = pd.read_csv(
    "data-science/data/hw_exam_grades.csv",
    converters={"SID": str.lower},
    usecols=lambda x: "Submission" not in x,
    index_col="SID",
)

data1 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_1_grades.csv', usecols=["Grade", "Email"])
data2 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_2_grades.csv', usecols=["Grade", "Email"])
data3= pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_3_grades.csv', usecols=["Grade", "Email"])
data4 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_4_grades.csv', usecols=["Grade", "Email"])
data5 = pd.read_csv('/Users/mac/Documents/GitHub/data-science/data/quiz_5_grades.csv', usecols=["Grade", "Email"])

data1.rename(columns = {'Grade':'Quiz1'}, inplace = True)
data2.rename(columns = {'Grade':'Quiz2'}, inplace = True)
data3.rename(columns = {'Grade':'Quiz3'}, inplace = True)
data4.rename(columns = {'Grade':'Quiz4'}, inplace = True)
data5.rename(columns = {'Grade':'Quiz5'}, inplace = True)

quiz_grades = pd.merge(
    data1,data2, on="Email"
)

quiz_grades = pd.merge(
    quiz_grades,data3, on="Email"
)

quiz_grades = pd.merge(
    quiz_grades,data4, on="Email"
)

quiz_grades = pd.merge(
    quiz_grades,data5, on="Email"
)

final_data = pd.merge(
    roster,
    hw_exam_grades,
    left_index=True,
    right_index=True,
)
final_data = pd.merge(
    final_data, quiz_grades, left_on="Email Address", right_on="Email"
)
final_data = final_data.fillna(0)


final_data.drop(columns=["Section", "Email"], inplace=True)



# final_data['Homework grade'] = (final_data['Homework 1'] / final_data['Homework 1 - Max Points'] 
# + final_data['Homework 2'] / final_data['Homework 2 - Max Points']
# + final_data['Homework 3'] / final_data['Homework 3 - Max Points']
# + final_data['Homework 4'] / final_data['Homework 4 - Max Points']
# + final_data['Homework 5'] / final_data['Homework 5 - Max Points']
# + final_data['Homework 6'] / final_data['Homework 6 - Max Points']
# + final_data['Homework 7'] / final_data['Homework 7 - Max Points']
# + final_data['Homework 8'] / final_data['Homework 8 - Max Points']
# + final_data['Homework 9'] / final_data['Homework 9 - Max Points']
# + final_data['Homework 10'] / final_data['Homework 10 - Max Points']) * 5

# final_data.drop(columns=["Homework 1", "Homework 1 - Max Points",
# "Homework 2", "Homework 2 - Max Points",
# "Homework 3", "Homework 3 - Max Points",
# "Homework 4", "Homework 4 - Max Points",
# "Homework 5", "Homework 5 - Max Points",
# "Homework 6", "Homework 6 - Max Points",
# "Homework 7", "Homework 7 - Max Points",
# "Homework 8", "Homework 8 - Max Points",
# "Homework 9", "Homework 9 - Max Points",
# "Homework 10", "Homework 10 - Max Points"], inplace=True)

hwGrade = 0
for i in range(1, 11):
    hwGrade += final_data[f"Homework {i}"]/final_data[f"Homework {i} - Max Points"]
    final_data.drop(columns=[f"Homework {i}", f"Homework {i} - Max Points"], inplace=True)
final_data['Homework Grade'] = hwGrade*9

examGrade = 0
for i in range(1, 4):
    examGrade += final_data[f"Exam {i}"]/final_data[f"Exam {i} - Max Points"]
    final_data.drop(columns=[f"Exam {i}", f"Exam {i} - Max Points"], inplace=True)
final_data['Exam Grade'] = examGrade*5

quizGrade = 0
for i in range(1, 6):
    qgrades = np.array(final_data[f'Quiz{i}'])
    quizGrade += final_data[f"Quiz{i}"]/qgrades.max()
    final_data.drop(columns=[f"Quiz{i}"], inplace=True)
final_data['Quiz Grade'] = quizGrade*3

finalGrade = 0
finalGrade += final_data["Homework Grade"] + final_data["Exam Grade"] + final_data["Quiz Grade"]
final_data['Final Grade'] = finalGrade

# final_data['Exam grade'] = (final_data['Exam 1'] / final_data['Exam 1 - Max Points'] 
# + final_data['Homework 2'] / final_data['Homework 2 - Max Points']
# + final_data['Homework 3'] / final_data['Homework 3 - Max Points']
# + final_data['Homework 4'] / final_data['Homework 4 - Max Points']
# + final_data['Homework 5'] / final_data['Homework 5 - Max Points']
# + final_data['Homework 6'] / final_data['Homework 6 - Max Points']
# + final_data['Homework 7'] / final_data['Homework 7 - Max Points']
# + final_data['Homework 8'] / final_data['Homework 8 - Max Points']
# + final_data['Homework 9'] / final_data['Homework 9 - Max Points']
# + final_data['Homework 10'] / final_data['Homework 10 - Max Points']) * 5

# final_data.drop(columns=["Homework 1", "Homework 1 - Max Points",
# "Homework 2", "Homework 2 - Max Points"
# "Homework 3", "Homework 3 - Max Points"
# "Homework 4", "Homework 4 - Max Points"
# "Homework 5", "Homework 5 - Max Points"
# "Homework 6", "Homework 6 - Max Points"
# "Homework 7", "Homework 7 - Max Points"
# "Homework 8", "Homework 8 - Max Points"
# "Homework 9", "Homework 9 - Max Points"
# "Homework 10", "Homework 10 - Max Points"], inplace=True)

print(final_data.head(3))