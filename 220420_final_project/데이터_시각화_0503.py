# -*- coding: utf-8 -*-
"""데이터_시각화_0503.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17nxYUyCUxxXBdApoDqG1PxwvYyZ4h6Yf

# 변수 설명
- **컬럼명 (컬럼 해석) : (데이터타입) 데이터 내용 (데이터 개수) "레이블"**

```
- index : (int64) 0 ~ 26456
- gender (성별) : (object) 
                 F(17697), M(8760)
- car (차량소유여부) : (object) 
                    Y(10047), N(16410)
- reality (부동산 소유 여부) : (object) 
                            Y(17830), N(8627)
- child_num (자녀수) : (int64) 
                      0(18340), 1(5386), 2(2362), 3(306), 
                      4(47), 5(10), 14(3), 7(2), 19(1)
- income_total (연간 소득): (float64)
- income_type (소득 분류) : (object) 
                          Working(13645) "4",
                          Commercial associate(6202) "0", 
                          Pensioner(4449) "1", 
                          State servant(2154) "2", 
                          Student(7) "3"
- edu_type (교육 수준) : (object) 
                        Secondary / secondary special(17995),
                        Higher education(7162), 
                        Incomplete higher(1020), 
                        Lower secondary(257), 
                        Academic degree(23)
- family_type (결혼 여부) : (object) 
                          Married 기혼(18196), 
                          Single / not married 미혼(3496), 
                          Civil marriage 동거혼?(2123), 
                          Separated 이혼(1539), Widow 미망인(1103)
- house_type (생활 방식) : (object)
                          House / apartment 자가(23653), 
                          With parents(1257), 
                          Municipal apartment 시립 아파트(818),
                          Rented apartment 임대 아파트(429),
                          Office apartment 사옥(190), 
                          Co-op apartment 주택조합 아파트(110)
- DAYS_BIRTH (출생일) : (int64)
                      0부터 역으로 셈. 
                      -1은 데이터 수집일 하루 전에 태어났음을 의미.
- DAYS_EMPLOYED (업무 시작일) : (int64)
                            0부터 역으로 셈. 
                            -1은 데이터 수집일 하루 전부터 일을 시작함을 의미. 
                            양수값은 고용되지 않은 상태를 의미.
- FLAG_MOBIL (핸드폰 소유 여부) : (int64) 
                              1(26457)
- work_phone (업무용 전화 소유 여부) : (int64) 
                                  0(20511), 1(5946)
- phone (가정용 전화 소유 여부) : (int64) 
                              0(18672), 1(7785)
- email (이메일 소유 여부) : (int64) 
                          0(24042), 1(2415)
- occyp_type (직업 유형) : (object) 
                        [nan, 'Laborers', 'Managers', 
                        'Sales staff', 'High skill tech staff',
                        'Core staff', 'Drivers', 
                        'Medicine staff', 'Accountants', 
                        'Realty agents', 'Security staff',
                        'Cleaning staff', 
                        'Private service staff', 
                        'Cooking staff', 'Secretaries', 
                        'HR staff', 'IT staff', 
                        'Low-skill Laborers', 
                        'Waiters/barmen staff']
- family_size (가족 규모) : (float64)
                          2.0(14106), 1.0(5109), 3.0(4632), 
                          4.0(2260), 5.0(291), 6.0(44), 7.0(9),
                          15.0(3), 9.0(2), 20.0(1)
- begin_month (신용카드 발급 월) : (float64)
                                0부터 역으로 셈. 
                                -1은 데이터 수집일 한달 전에 신용카드를 발급받음을 의미.
- credit (신용카드 대금 연체를 기준으로 한 신용도 ) : (float64)
                                              낮을수록 높은 신용의 신용카드 사용자 의미.)  
                                              0, 1, 2
```

# 데이터 불러오기
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

# path = '/content/drive/MyDrive/final_project/data/'
path = '/content/drive/MyDrive/[멀캠 파이널 프로젝트] 신용카드 연체 예측/data/'

train = pd.read_csv(path + 'train.csv')
test = pd.read_csv(path + 'test.csv')

train

train.isnull().sum()

train.info()

train.describe(include='all')

"""## 중복행에 관하여
- credit은 사용자의 신용카드 대금 연체를 기준으로 한 신용도이다.
- 즉 동일인이어도 카드에 따라, 또 시점에 따라 연체 대금 연체 정도가 다를 수 있습니다.

# 데이터 전처리

## 결측값
- occyp_type 값 채우기
```
occyp_type 이 결측값인 사람들의 자료 확인 —> 무직인 것인지 단순한 결측값인지 확인 
—> 무직을 연금 수령자라고 가정 —> 무직(연금)이라면 고용 날짜가 양수이여야 함 
—> 연금 수령자인 사람들 중에 날짜가 음수인 사람들은 이상치로 판단하여 제거 
—> 무직인 사람들은 NaN값으로 18 부여 —> 고용 날짜가 음수인 사람은 직업이 있다고 가정 
—> 그 사람들끼리 그룹으로 모아 특성 파악 후 직업 부여
```
"""

# occyp_type이 결측인 행 추출
condition = train['occyp_type'].isnull()
nan_occyp_type = train.loc[condition]
# df = df.drop(['child_num', 'edu_type', 'family_type', 'house_type', 'gender', 'FLAG_MOBIL', 'begin_month', 'family_size', 'index', 'email'] ,axis = 1)
nan_occyp_type

# occyp_type이 결측이면서 income_type이 Pensioner(연금수령자)인 행 추출
df_Pensioner = nan_occyp_type[nan_occyp_type['income_type'] == 'Pensioner']
df_Pensioner

# 연금수령자인데 DAYS_EMPLOYED가 0 이상인 사람은 이상치로 제거 (무직으로 판단 X)
con = df_Pensioner['DAYS_EMPLOYED'] < 0
Pensioner_n = df_Pensioner.loc[con]
Pensioner_n

# DAYS_EMPLOYED가 365243아닌 값이 추가적으로 있는지 확인
# 음수인 사람만이 365243 아닌 것을 확인
con = df_Pensioner['DAYS_EMPLOYED'] != 365243
Pensioner_n = df_Pensioner.loc[con]
Pensioner_n

"""### occyp_type 이상치 제거
- 연금으로 인해 소득이 들어오는 사람을 무직이라고 가정
- 무직임에도 고용 기간이 음수인 사람은 이상치로 판단
"""

# 연금받는 사람들은 무직으로 처리하여 NaN 값 부여
# 레이블 시 자동으로 18 부여
train_del_2 = train.drop(train.index[6743])
train_del_2 = train_del_2.drop(train.index[15682])
train_del_2

"""- 이상치 제거 한 자료에 나이 파생변수"""

train_del_2['DAYS_BIRTH'] = round(train_del_2['DAYS_BIRTH']/-365)
train_del_2

"""### occyp_type 결측치 채우기
- 소득 분류가 연금이 아닌 사람들의 직업 채우기
- 클러스터링

#### 무직자 채우기
- 연금을 받는 사람들 중에 근로 일자가 양수인 사람들을 무직(no_job)으로 채움
- 연금 이상치 제거 + 무직자 등록
"""

train_copy = train_del_2.copy()
train_copy.loc[train_copy['income_type'] == 'Pensioner', 'occyp_type'] = 'no_job'
train_copy

train_copy[train_copy['income_type'] == 'Pensioner']

"""#### 나머지 결측값 처리
- 무직자가 아님에도 직업이 결측인 값 처리

## object 타입 레이블 인코딩
- gender (성별)
```
0 : F 
1 : M 
```
- car (차량 소유 여부)
```
0 : N 
1 : Y 
```
- reality (부동산 소유 여부)
```
0 : N 
1 : Y 
```
- income_type (소득 분류)
```
0 : Commercial associate
1 : Pensioner  
2 : State servant        
3 : Student              
4 : Working              
```
- edu_type (교육 수준)
```
0 : Academic degree               
1 : Higher education              
2 : Incomplete higher             
3 : Lower secondary               
4 : Secondary / secondary 
```
- family_type (결혼 여부)
```
0 : Civil marriage          
1 : Married               
2 : Separated                
3 : Single / not married     
4: Widow                    
```
- house_type (생활 방식)
```
0 : Co-op apartment          
1: House / apartment      
2: unicipal apartment      
3: Office apartment         
4: Rented apartment         
5: With parents            
```
- occyp_type (직업 유형)
```
0 : Accountants               
1 : Cleaning staff            
2 : Cooking staff             
3 : Core staff               
4 : Drivers                  
5 : High skill tech staff    
6 : HR staff                   
7 : IT staff                   
8 : Laborers                 
9 : Low-skill Laborers        
10 : no_job
11 : Managers                 
12 : Medicine staff            
13 : Private service staff     
14 : Realty agents              
15 : Sales staff              
16 : Secretaries                
17 : Security staff            
18 : Waiters/barmen staff      
```
"""

# gender 성별
print(train_copy.gender.unique())
print(train_copy['gender'].value_counts())

# car 차량 소유 여부
print(train_copy.car.unique())
print(train_copy['car'].value_counts())

# reality 부동산 소유 여부 
print(train_copy.reality.unique())
print(train_copy['reality'].value_counts())

# income_type 소득 분류 종류 (5가지)
print(train_copy.income_type.unique())
print(train_copy['income_type'].value_counts())

# edu_type 교육 수준 종류 (5가지)
print(train_copy.edu_type.unique())
print(train_copy['edu_type'].value_counts())

# family_type 결혼 여부 종류 (5가지)
print(train_copy.family_type.unique())
print(train_copy['family_type'].value_counts())

# house_type 생활 방식 종류 (6가지)
print(train_copy.house_type.unique())
print(train_copy['house_type'].value_counts())

# occyp_type 직업 유형 종류 (nan 제외 18가지)
print(train_copy.occyp_type.unique())
print(train_copy['occyp_type'].value_counts())

processed_data = train_copy.copy()
encoder = LabelEncoder()

def encoding(feat):
  encoder.fit(processed_data[feat])
  processed_data[feat] = encoder.transform(processed_data[feat])
  pass

encoding('gender')
encoding('car')
encoding('reality')
encoding('income_type')
encoding('edu_type')
encoding('family_type')
encoding('house_type')
encoding('occyp_type')

processed_data

# processed_data = processed_data.astype({'income_total':int, 'DAYS_BIRTH':int})
processed_data = processed_data.drop(['index', 'FLAG_MOBIL'], axis=1)
processed_data

processed_data[processed_data['DAYS_EMPLOYED'] > 0]

processed_data[processed_data['income_type'] == 1]

processed_data[(processed_data['income_type'] == 1) & (processed_data['DAYS_EMPLOYED'] > 0)]



processed_data[processed_data['income_type'] == 1]

"""## KNN으로 결측치 채우기
- 직업의 특성을 파악하여 비슷한 특성으로 occyp_type 결측치 채우기
"""

from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 3, weights = "distance")

# 결측값 데이터 프레임
con = processed_data['occyp_type'] == 19
knn_test = processed_data.loc[con]
knn_test

# 정규화
def min_max_normalize(lst):
    normalized = []
    
    for value in lst:
        normalized_num = (value - min(lst)) / (max(lst) - min(lst))
        normalized.append(normalized_num)
    
    return normalized

# 19 데이터 제거 df
knn_train = processed_data[processed_data['occyp_type'] != 19]
knn_train = processed_data[processed_data['occyp_type'] != 10]
knn_train

knn_train = knn_train.drop(['begin_month'], axis=1)
knn_train

# 정확도 측정을 위한 데이터셋
from sklearn.model_selection import train_test_split

feature = knn_train.drop('occyp_type', axis=1)
target = knn_train['occyp_type']

x_train, x_test, y_train, y_test = train_test_split(feature, target, test_size=0.2, random_state=100)

knn_train.head()

from sklearn.preprocessing import MinMaxScaler

# 정규화 작업
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

pd.DataFrame(x_train, columns = knn_train.columns[:-1]).head()

from sklearn.neighbors import KNeighborsClassifier

# kNN 모델 선언
k = 3
model = KNeighborsClassifier(n_neighbors = k)
# 모델 학습
model.fit(x_train, y_train)

from sklearn.metrics import accuracy_score

y_pred = model.predict(x_test)
accuracy_score(y_test, y_pred)

knn_test = knn_test.drop(['begin_month', 'occyp_type'], axis=1)
knn_pred = model.predict(knn_test)
knn_test['class'] = knn_pred

knn_test



"""## 데이터 불균형 해결"""





processed_data_del = processed_data[['income_total', 'income_type', 'DAYS_BIRTH']]
processed_data_del

# pro_occyp_type = processed_data_del[processed_data_del['occyp_type'] == 8]
# pro_occyp_type

# sns.pairplot(pro_occyp_type)
# plt.title("0")
# plt.show()

# sns.pairplot(pro_occyp_type, hue="occyp_type", markers=["o"])
# plt.title("0")
# plt.show()

# k-mean
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=18, init='k-means++', max_iter=300,random_state=0)
kmeans.fit(processed_data_del)

KMeans(n_clusters=18, random_state=0)

processed_data_del['target'] = processed_data.occyp_type
processed_data_del['cluster']=kmeans.labels_
credit_result = processed_data_del.groupby(['target','cluster'])['income_total'].count()
print(credit_result)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca_transformed = pca.fit_transform(processed_data_del)

processed_data_del['pca_x'] = pca_transformed[:,0]
processed_data_del['pca_y'] = pca_transformed[:,1]
processed_data_del.head(3)

# cluster 값이 0, 1, 2 인 경우마다 별도의 Index로 추출
marker0_ind = processed_data_del[processed_data_del['cluster']==0].index
marker1_ind = processed_data_del[processed_data_del['cluster']==1].index
marker2_ind = processed_data_del[processed_data_del['cluster']==2].index
marker3_ind = processed_data_del[processed_data_del['cluster']==3].index
marker4_ind = processed_data_del[processed_data_del['cluster']==4].index
marker5_ind = processed_data_del[processed_data_del['cluster']==5].index
marker6_ind = processed_data_del[processed_data_del['cluster']==6].index
marker7_ind = processed_data_del[processed_data_del['cluster']==7].index
marker8_ind = processed_data_del[processed_data_del['cluster']==8].index
marker9_ind = processed_data_del[processed_data_del['cluster']==9].index
marker10_ind = processed_data_del[processed_data_del['cluster']==10].index
marker11_ind = processed_data_del[processed_data_del['cluster']==11].index
marker12_ind = processed_data_del[processed_data_del['cluster']==12].index
marker13_ind = processed_data_del[processed_data_del['cluster']==13].index
marker14_ind = processed_data_del[processed_data_del['cluster']==14].index
marker15_ind = processed_data_del[processed_data_del['cluster']==15].index
marker16_ind = processed_data_del[processed_data_del['cluster']==16].index
marker17_ind = processed_data_del[processed_data_del['cluster']==17].index

# cluster값 0, 1, 2에 해당하는 Index로 각 cluster 레벨의 pca_x, pca_y 값 추출. o, s, ^ 로 marker 표시
plt.scatter(x=processed_data_del.loc[marker0_ind,'pca_x'], y=processed_data_del.loc[marker0_ind,'pca_y'], marker='o') 
plt.scatter(x=processed_data_del.loc[marker1_ind,'pca_x'], y=processed_data_del.loc[marker1_ind,'pca_y'], marker='v')
plt.scatter(x=processed_data_del.loc[marker2_ind,'pca_x'], y=processed_data_del.loc[marker2_ind,'pca_y'], marker='^')
plt.scatter(x=processed_data_del.loc[marker3_ind,'pca_x'], y=processed_data_del.loc[marker3_ind,'pca_y'], marker='<')
plt.scatter(x=processed_data_del.loc[marker4_ind,'pca_x'], y=processed_data_del.loc[marker4_ind,'pca_y'], marker='>')
plt.scatter(x=processed_data_del.loc[marker5_ind,'pca_x'], y=processed_data_del.loc[marker5_ind,'pca_y'], marker='8')
plt.scatter(x=processed_data_del.loc[marker6_ind,'pca_x'], y=processed_data_del.loc[marker6_ind,'pca_y'], marker='s')
plt.scatter(x=processed_data_del.loc[marker7_ind,'pca_x'], y=processed_data_del.loc[marker7_ind,'pca_y'], marker='p')
plt.scatter(x=processed_data_del.loc[marker8_ind,'pca_x'], y=processed_data_del.loc[marker8_ind,'pca_y'], marker='*')
plt.scatter(x=processed_data_del.loc[marker9_ind,'pca_x'], y=processed_data_del.loc[marker9_ind,'pca_y'], marker='h')
plt.scatter(x=processed_data_del.loc[marker10_ind,'pca_x'], y=processed_data_del.loc[marker10_ind,'pca_y'], marker='H')
plt.scatter(x=processed_data_del.loc[marker11_ind,'pca_x'], y=processed_data_del.loc[marker11_ind,'pca_y'], marker='D')
plt.scatter(x=processed_data_del.loc[marker12_ind,'pca_x'], y=processed_data_del.loc[marker12_ind,'pca_y'], marker='d')
plt.scatter(x=processed_data_del.loc[marker13_ind,'pca_x'], y=processed_data_del.loc[marker13_ind,'pca_y'], marker='P')
plt.scatter(x=processed_data_del.loc[marker14_ind,'pca_x'], y=processed_data_del.loc[marker14_ind,'pca_y'], marker='X')
plt.scatter(x=processed_data_del.loc[marker15_ind,'pca_x'], y=processed_data_del.loc[marker15_ind,'pca_y'], marker='+')
plt.scatter(x=processed_data_del.loc[marker16_ind,'pca_x'], y=processed_data_del.loc[marker16_ind,'pca_y'], marker='1')
plt.scatter(x=processed_data_del.loc[marker17_ind,'pca_x'], y=processed_data_del.loc[marker17_ind,'pca_y'], marker='2')

plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.title('3 Clusters Visualization by 2 PCA Components')
plt.show()

# sns.pairplot(df_test, hue="occyp_type", markers=["o"])
# plt.title("0")
# plt.show()

# k-mean
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=18, init='k-means++', max_iter=300,random_state=0)
kmeans.fit(processed_data_del)

KMeans(n_clusters=18, random_state=0)

processed_data_del['target'] = processed_data.occyp_type
processed_data_del['cluster']=kmeans.labels_
credit_result = processed_data_del.groupby(['target','cluster'])['income_total'].count()
print(credit_result)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca_transformed = pca.fit_transform(processed_data_del)

processed_data_del['pca_x'] = pca_transformed[:,0]
processed_data_del['pca_y'] = pca_transformed[:,1]
processed_data_del.head(3)

# cluster 값이 0, 1, 2 인 경우마다 별도의 Index로 추출
marker0_ind = processed_data_del[processed_data_del['cluster']==0].index
marker1_ind = processed_data_del[processed_data_del['cluster']==1].index
marker2_ind = processed_data_del[processed_data_del['cluster']==2].index
marker3_ind = processed_data_del[processed_data_del['cluster']==3].index
marker4_ind = processed_data_del[processed_data_del['cluster']==4].index
marker5_ind = processed_data_del[processed_data_del['cluster']==5].index
marker6_ind = processed_data_del[processed_data_del['cluster']==6].index
marker7_ind = processed_data_del[processed_data_del['cluster']==7].index
marker8_ind = processed_data_del[processed_data_del['cluster']==8].index
marker9_ind = processed_data_del[processed_data_del['cluster']==9].index
marker10_ind = processed_data_del[processed_data_del['cluster']==10].index
marker11_ind = processed_data_del[processed_data_del['cluster']==11].index
marker12_ind = processed_data_del[processed_data_del['cluster']==12].index
marker13_ind = processed_data_del[processed_data_del['cluster']==13].index
marker14_ind = processed_data_del[processed_data_del['cluster']==14].index
marker15_ind = processed_data_del[processed_data_del['cluster']==15].index
marker16_ind = processed_data_del[processed_data_del['cluster']==16].index
marker17_ind = processed_data_del[processed_data_del['cluster']==17].index

# cluster값 0, 1, 2에 해당하는 Index로 각 cluster 레벨의 pca_x, pca_y 값 추출. o, s, ^ 로 marker 표시
plt.scatter(x=processed_data_del.loc[marker0_ind,'pca_x'], y=processed_data_del.loc[marker0_ind,'pca_y'], marker='o') 
plt.scatter(x=processed_data_del.loc[marker1_ind,'pca_x'], y=processed_data_del.loc[marker1_ind,'pca_y'], marker='v')
plt.scatter(x=processed_data_del.loc[marker2_ind,'pca_x'], y=processed_data_del.loc[marker2_ind,'pca_y'], marker='^')
plt.scatter(x=processed_data_del.loc[marker3_ind,'pca_x'], y=processed_data_del.loc[marker3_ind,'pca_y'], marker='<')
plt.scatter(x=processed_data_del.loc[marker4_ind,'pca_x'], y=processed_data_del.loc[marker4_ind,'pca_y'], marker='>')
plt.scatter(x=processed_data_del.loc[marker5_ind,'pca_x'], y=processed_data_del.loc[marker5_ind,'pca_y'], marker='8')
plt.scatter(x=processed_data_del.loc[marker6_ind,'pca_x'], y=processed_data_del.loc[marker6_ind,'pca_y'], marker='s')
plt.scatter(x=processed_data_del.loc[marker7_ind,'pca_x'], y=processed_data_del.loc[marker7_ind,'pca_y'], marker='p')
plt.scatter(x=processed_data_del.loc[marker8_ind,'pca_x'], y=processed_data_del.loc[marker8_ind,'pca_y'], marker='*')
plt.scatter(x=processed_data_del.loc[marker9_ind,'pca_x'], y=processed_data_del.loc[marker9_ind,'pca_y'], marker='h')
plt.scatter(x=processed_data_del.loc[marker10_ind,'pca_x'], y=processed_data_del.loc[marker10_ind,'pca_y'], marker='H')
plt.scatter(x=processed_data_del.loc[marker11_ind,'pca_x'], y=processed_data_del.loc[marker11_ind,'pca_y'], marker='D')
plt.scatter(x=processed_data_del.loc[marker12_ind,'pca_x'], y=processed_data_del.loc[marker12_ind,'pca_y'], marker='d')
plt.scatter(x=processed_data_del.loc[marker13_ind,'pca_x'], y=processed_data_del.loc[marker13_ind,'pca_y'], marker='P')
plt.scatter(x=processed_data_del.loc[marker14_ind,'pca_x'], y=processed_data_del.loc[marker14_ind,'pca_y'], marker='X')
plt.scatter(x=processed_data_del.loc[marker15_ind,'pca_x'], y=processed_data_del.loc[marker15_ind,'pca_y'], marker='+')
plt.scatter(x=processed_data_del.loc[marker16_ind,'pca_x'], y=processed_data_del.loc[marker16_ind,'pca_y'], marker='1')
plt.scatter(x=processed_data_del.loc[marker17_ind,'pca_x'], y=processed_data_del.loc[marker17_ind,'pca_y'], marker='2')

plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.title('3 Clusters Visualization by 2 PCA Components')
plt.show()

train_label = pd.read_csv(path + 'train.csv')
encoder = LabelEncoder()

# gender 라벨링
encoder.fit(train_label['gender'])
train_label['gender'] = encoder.transform(train_label['gender'])

# car 라벨링
encoder.fit(train_label['car'])
train_label['car'] = encoder.transform(train_label['car'])

# reality 라벨링
encoder.fit(train_label['reality'])
train_label['reality'] = encoder.transform(train_label['reality'])

# income_type 라벨링
encoder.fit(train_label['income_type'])
train_label['income_type'] = encoder.transform(train_label['income_type'])

# edu_type 라벨링
encoder.fit(train_label['edu_type'])
train_label['edu_type'] = encoder.transform(train_label['edu_type'])

# family_type 라벨링
encoder.fit(train_label['family_type'])
train_label['family_type'] = encoder.transform(train_label['family_type'])

# house_type 라벨링
encoder.fit(train_label['house_type'])
train_label['house_type'] = encoder.transform(train_label['house_type'])

# occyp_type 라벨링
encoder.fit(train_label['occyp_type'])
train_label['occyp_type'] = encoder.transform(train_label['occyp_type'])

train_label



train_label.corr()

import seaborn as sns
import matplotlib.pyplot as plt

corr_label = train_label.corr()

sns.heatmap(corr_label)









train.columns

train.info()

train['occyp_type']

# sns.countplot(x='occyp_type', y='', data=train)



"""# 데이터 시각화

1.   // 고용되기 전까지의 일수
2.   // 나이, 태어난 월, 태어난 주(출생연도의 n주차) : 날짜가 데이터가 들어가면 성능이 더 좋아짐
3.   // 근속연수, 고용된 달, 고용된 주(고용연도의 n주차)
4.   ability?// 소득/(살아온 일수+근무일수)
5.   income_mean?// 소득/가족 수
6.   ID 생성 : 각 컬럼의 값들을 더해서 고유한 사람들 파악(한 사람이 여러 개 카드를 만들 가능성을 고려해 begin_month는 제외함)




"""

train[''] = train['income_total'] / (train['DAYS_BIRTH'] + train['DAYS_EMPLOYED'])

train2 = train.copy()
# train2['DAYS_BIRTH'] = round(train['DAYS_BIRTH']/-365)
train2['DAYS_BIRTH'] = train2['DAYS_BIRTH']//-365

# 양수
feats = ['DAYS_BIRTH', 'begin_month', 'DAYS_EMPLOYED']
for feat in feats:
    train2[feat]=np.abs(train2[feat])
    test[feat]=np.abs(test[feat])

train2.head(2)

train2['DAYS_EMPLOYED'] = train2['DAYS_EMPLOYED']//-365
train2.head(2)

# 4438명
train2[(train2['DAYS_EMPLOYED'] >= 0)]

"""##4438명 = 0이상인 사람들은 365243값만 있음"""

# 4438 
train2[(train2['DAYS_EMPLOYED'] == 365243)]

train2[(train2['DAYS_EMPLOYED'] == 365243)]['DAYS_BIRTH'].value_counts()

# 연금수령자만 존재, 나이대 불균형, 'DAYS_EMPLOYED' = 양수값
train2[train2['DAYS_EMPLOYED'] == 365243]['income_type'].value_counts()

train2['child_num'].value_counts()

# 자녀수 7명, 14명, 19명 제거
train2 = train2[train2['child_num'] < 7]
train2['child_num'].value_counts()

train2['pre_EMPLOYED'] = train2[]

"""---"""

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
x = encoder.fit_transform(train['occyp_type'])

plt.scatter(x, train['income_total'], alpha=0.1)



sns.boxplot(x='occyp_type', y='income_total', data=train)

train['occyp_type'].value_counts()

list(enumerate(list(encoder.classes_)))

train['occyp_type'].value_counts()

train['occyp_type'].hist()

train['credit'] = train['credit'].astype(int)

train.income_type.unique()

cond_list = [(train[train['income_type']==value], value) for value in train.income_type.unique()]

len(cond_list)

train.corr()['DAYS_EMPLOYED']



fig, axes = plt.subplots(len(cond_list),1, figsize=(15,10))
for i in range(len(cond_list)):
  sns.countplot(x='occyp_type', data=cond_list[i][0], order=train['occyp_type'].value_counts().index, ax=axes[i])
  axes[i].title.set_text(cond_list[i][1])

cond_list = [train[train['credit']==2], train[train['credit']==1], 
             train[train['credit']==0]]

sns.countplot?

sns.countplot(x='occyp_type', data=train, order=train['occyp_type'].value_counts().index)

train['occyp_type'].value_counts()

fig, axes = plt.subplots(3,1, figsize=(15,10))
for i in range(3):
  sns.countplot(x='occyp_type', data=cond_list[i], order=train['occyp_type'].value_counts().index, ax=axes[i])





plt.scatter(x, train['credit'], alpha=0.01)

train['credit'].value_counts()



















