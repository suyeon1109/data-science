import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree  #시각화 툴
from sklearn.metrics import accuracy_score

test = pd.read_csv('/Users/mac/Downloads/open/test.csv')
train = pd.read_csv('/Users/mac/Downloads/open/train.csv',usecols=['성별','차량 소유 여부', '부동산 소유 여부', '자녀 수', '연간 수입', '수입 유형','TARGET'])
# train.info()

X = train.iloc[:, 1:7]
y = train['TARGET']

X['성별'] = X['성별'].map({'여성': 1, '남성': 0, '기타':2})
X['수입 유형'] = X['수입 유형'].map({'연금수령자':0 , '근로자':1, '기타':2, '공무원':3, '실직자':4, '학생':5, '사업가':6})

# print(X.isnull().values.any())
# invalid_rows = [index for index, row in X.iterrows() if row.isnull().any()]
# print(invalid_rows)
# # X.dropna(axis=0)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42)


# df = X['성별']
# income_list=[]
# for each in df:
#     if each not in income_list:
#         income_list.append(each)
# print(income_list)

# df = train['산업군']
# field_list=[]
# for each in df:
#     if each not in field_list:
#         field_list.append(each)
# print(field_list)

# train['산업군'] = train['산업군'].map({'기타 1', '사업 1', '사업 0', '산업 4', '사업 2', '무역 0', '전기', '운송 1', '학교', '의학', 
# '자영업', '대학교', '산업 3', '군대', '기타 0', '레스토랑', '산업 10', '경찰', '은행', '통신', '정부', '운송 0', '운송 2', '건설', '산업 8', 
# '무역 3', '산업 7', '문화', '호텔', '주택', '유치원', '우체부', '보안', '농업', '무역 6', '국가 안보', '무역 2', '산업 2', '보험', '서비스', 
# '산업 9', '무역 4', '광고', '무역 1', '무역 5', '환경', '산업 6', '산업 0', '산업 1', '부동산 중개업', '산업 5', '법률 서비스', '운송 3', 
# '모바일', '종교', '산업 12'})


classifier_rf = RandomForestClassifier(random_state=42, n_jobs=-1, max_depth=5, n_estimators=100, oob_score=True)

classifier_rf.fit(X_train, y_train)

predicted = classifier_rf.predict(X_test)
accuracy = accuracy_score(y_test, predicted)

print(f"Out-of-bag score estimate: {classifier_rf.oob_score_:.3}")
print(f"Mean accuracy score: {accuracy:.3}")