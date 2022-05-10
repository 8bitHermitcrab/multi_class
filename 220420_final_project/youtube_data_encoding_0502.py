# -*- coding: utf-8 -*-
"""youtube_data_encoding_0502.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UdsyyVG5CQ1i1cTJMWKm2_EJ5d--9oZI

# 데이콘 유튜브
[신용카드 사용자 연체 예측 AI 데이터](https://dacon.io/competitions/official/235713/data)
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd

"""# 데이터 불러오기

레이블 인코딩, 원-핫 인코딩
직업 여부 결측치 제거, 직업 여부 값 대체

- **컬럼명 (컬럼 해석) : (데이터타입) 데이터 내용 (데이터 개수) "레이블"**


- index : (int64) 0 ~ 26456
- gender (성별) : (object) F(17697), M(8760) 
- car (차량소유여부) : (object) Y(10047), N(16410)
- reality (부동산 소유 여부) : (object) Y(17830), N(8627)
- child_num (자녀수) : (int64) 0(18340), 1(5386), 2(2362), 3(306), 4(47), 5(10), 14(3), 7(2), 19(1)
- income_total (연간 소득): (float64)
- income_type (소득 분류) : (object) Working(13645) "4", Commercial associate(6202) "0", Pensioner 연금수급자(4449) "1", State servant 공무원(2154) "2", Student(7) "3"
- edu_type (교육 수준) : (object) Secondary / secondary special(17995), Higher education(7162), Incomplete higher(1020), Lower secondary(257), Academic degree(23)
- family_type (결혼 여부) : (object) Married 기혼(18196), Single / not married 미혼(3496), Civil marriage 동거혼?(2123), Separated 이혼(1539), Widow 미망인(1103)
- house_type (생활 방식) : (object)
House / apartment 자가(23653),With parents(1257), Municipal apartment 시립 아파트(818), Rented apartment 임대 아파트(429), Office apartment 사옥(190), Co-op apartment 주택조합 아파트(110)
- DAYS_BIRTH (출생일 : 0부터 역으로 셈. -1은 데이터 수집일 하루 전에 태어났음을 의미.) : (int64)
- DAYS_EMPLOYED (업무 시작일 : 0부터 역으로 셈. -1은 데이터 수집일 하루 전부터 일을 시작함을 의미. 양수값은 고용되지 않은 상태를 의미.) : (int64)
- FLAG_MOBIL (핸드폰 소유 여부) : (int64) 1(26457)
- work_phone (업무용 전화 소유 여부) : (int64) 0(20511), 1(5946)
- phone (가정용 전화 소유 여부) : (int64) 0(18672), 1(7785)
- email (이메일 소유 여부) : (int64) 0(24042), 1(2415)
- occyp_type (직업 유형) : (object) [nan, 'Laborers', 'Managers', 'Sales staff', 'High skill tech staff', 'Core staff', 'Drivers', 'Medicine staff', 'Accountants', 'Realty agents', 'Security staff', 'Cleaning staff', 'Private service staff', 'Cooking staff', 'Secretaries', 'HR staff', 'IT staff', 'Low-skill Laborers', 'Waiters/barmen staff']
- family_size (가족 규모) : (float64) 
2.0(14106), 1.0(5109), 3.0(4632), 4.0(2260), 5.0(291), 6.0(44), 7.0(9), 15.0(3), 9.0(2), 20.0(1)
- begin_month (신용카드 발급 월 : 0부터 역으로 셈. -1은 데이터 수집일 한달 전에 신용카드를 발급받음을 의미.) : (float64)
- credit (신용카드 대금 연체를 기준으로 한 신용도 : 낮을수록 높은 신용의 신용카드 사용자 의미.) : (float64) 0, 1, 2
"""

PATH = '/content/drive/MyDrive/[멀캠 파이널 프로젝트] 신용카드 연체 예측/data/'
train = pd.read_csv(PATH + 'train.csv')
train.head(2)

test = pd.read_csv(PATH + 'test.csv')
test.head(2)

sample = pd.read_csv(PATH + 'sample_submission.csv')
sample.head(2)

train.info()

train.describe()

train.shape, test.shape

train['credit'].unique()

"""train 19개 컬럼을 x, x를 모델에 넣고, y인 credit을 도출.

##06.train test 합치기
"""

data = pd.concat([train, test], axis = 0)
data.head(2)

data.isnull().sum()
# test에서 ['credit'] 컬럼의 10,000개 null 값

train['credit'].isnull().sum()

data1 = data.drop('occyp_type', axis = 1)
data1.isnull().sum()

"""##08.그룹나누기"""



"""---"""

import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

encoder = LabelEncoder()

train_label = pd.read_csv(PATH + 'train.csv')

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

sns.heatmap(train_label)
plt.show()

train.info()

train.tail(2)

train['gender'].value_counts()

train['car'].value_counts()

train['reality'].value_counts()

train['occyp_type'].value_counts()

train['income_type'].value_counts()

train['house_type'].unique()

train['house_type'].value_counts()

train['edu_type'].value_counts()

train['family_type'].value_counts()

train['house_type'].value_counts()

train['FLAG_MOBIL'].value_counts()

train['work_phone'].value_counts()

train['phone'].value_counts()

train['email'].value_counts()

train['family_size'].value_counts()

train['child_num'].value_counts()

# 레이블 인코딩


encoder = LabelEncoder()
encoder.fit(train[''])
encoder.transform(train[''])

train['DAYS_EMPLOYED'] >.bool()

train['occyp_type'].bool(True)

train['occyp_type'].notna()

df = train[['income_type','occyp_type']]
df[df['occyp_type'].isnull()]

train.tail()

train[(train['occyp_type'].isnull()) & (train['income_type'] == 'Pensioner') & (train['DAYS_EMPLOYED'] != 365243)]

train_label1 = train_label.loc[train_label['DAYS_EMPLOYED'] == 365243, .replace(365243, 0)

train_label

train_label1 = train_label.replace(365243, 0)
train_label1

train_label.corr()

train_label1.corr()
