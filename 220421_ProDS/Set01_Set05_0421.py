# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Administrator
"""

#%%

# =============================================================================
# =============================================================================
# # 문제 01 유형(DataSet_01.csv 이용)
#
# 구분자 : comma(“,”), 4,572 Rows, 5 Columns, UTF-8 인코딩
# 
# 글로벌 전자제품 제조회사에서 효과적인 마케팅 방법을 찾기
# 위해서 채널별 마케팅 예산과 매출금액과의 관계를 분석하고자
# 한다.
# 컬 럼 / 정 의  /   Type
# TV   /     TV 마케팅 예산 (억원)  /   Double
# Radio / 라디오 마케팅 예산 (억원)  /   Double
# Social_Media / 소셜미디어 마케팅 예산 (억원)  / Double
# Influencer / 인플루언서 마케팅
# (인플루언서의 영향력 크기에 따라 Mega / Macro / Micro / 
# Nano) / String

# SALES / 매출액 / Double
# =============================================================================
# =============================================================================



import pandas as pd
import numpy as np

data1 = pd.read_csv('//Users/kij/workspace/20220421_ProDS/Dataset/DataSet_01.csv')
data1.info()
data1.columns
# ['TV', 'Radio', 'Social_Media', 'Influencer', 'Sales']

data1.values  # numpy

#%%

# =============================================================================
# 1. 데이터 세트 내에 총 결측값의 개수는 몇 개인가? (답안 예시) 23
# =============================================================================

# 결측치가 포함된 셀의 수
data1.isna().sum().sum()

# 답: 26

# [참고] 
# 결측치가 포함된 행의 수
data1.isnull().any(axis=1).sum()


#%%

# =============================================================================
# 2. TV, Radio, Social Media 등 세 가지 다른 마케팅 채널의 예산과 매출액과의 상관분석을
# 통하여 각 채널이 매출에 어느 정도 연관이 있는지 알아보고자 한다. 
# - 매출액과 가장 강한 상관관계를 가지고 있는 채널의 상관계수를 소수점 5번째
# 자리에서 반올림하여 소수점 넷째 자리까지 기술하시오. (답안 예시) 0.1234
# =============================================================================
var_list=['TV', 'Radio', 'Social_Media', 'Sales']
q2_corr=data1[var_list].corr().drop('Sales')['Sales'].abs()


q2_corr.max() # 최대값
q2_corr.idxmax() # 최대값이 있는 인덱스명
q2_corr.argmax()  # 최대값이 있는 위치번호
q2_corr.nlargest(2).index

#  채널의 상관계수를 소수점 5번째
# 자리에서 반올림하여 소수점 넷째 자리까지 기술
round(q2_corr.max(), 4)

# 답: 0.9995

# np.round, np.floor(1.123456 * 100)/100, np.ceil, np.trunc(int)
#%%

# =============================================================================
# 3. 매출액을 종속변수, TV, Radio, Social Media의 예산을 독립변수로 하여 회귀분석을
# 수행하였을 때, 세 개의 독립변수의 회귀계수를 큰 것에서부터 작은 것 순으로
# 기술하시오. 
# - 분석 시 결측치가 포함된 행은 제거한 후 진행하며, 회귀계수는 소수점 넷째 자리
# 이하는 버리고 소수점 셋째 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================
from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols
from statsmodels.api import OLS, add_constant # 상수항 추가

# 1. LinearRegression

var_list = ['TV', 'Radio', 'Social_Media']

q3 = data1.dropna()
lm1 = LinearRegression(fit_intercept=True).fit(q3[var_list], q3['Sales'])

dir(lm1)

lm1.coef_ # 회귀계수
lm1.intercept_ # 절편

coef1 = pd.Series(lm1.coef_, index=var_list)
(np.floor(coef1.sort_values(ascending=False) * 1000) / 1000).values

# 답: 3.562, 0.004, -0.004

# 2. ols
# ols1 = ols('y~ x1 + x2 +C(cat1)-1', 데이터셋명) # C = 카테고리 변수
# ols2 = ols1.fit()

form1 = 'Sales~TV+Radio+Social_Media'

lm2 = ols(form1, q3).fit()

# lm2 = ols(form1, q3)
# lm3 = lm2.fit()


dir(lm2)
lm2.summary()
lm2.params
# 이상치 제외한 데이터
outlier_drop_data = q3[lm2.outlier_test()['bonf(p)'] >= 0.05]
lm2.rsquared

lm2.pvalues.index[lm2.pvalues < 0.05]

lm3 = ols('Sales~TV-1', q3).fit()
lm3.summary()

# 3. OLS : 상수항 미포함
xx = add_constant(q3[var_list])
lm4 = OLS(q3['Sales'], xx).fit()

lm4.summary()

# 범주형
var_list = q3.columns.drop('Sales')
form2 = 'Sales~' + '+'.join(var_list)

lm5 = ols(form2, q3).fit()

lm5.summary()
q3.Influencer.unique()

#%%

# =============================================================================
# =============================================================================
# # 문제 02 유형(DataSet_02.csv 이용)
# 구분자 : comma(“,”), 200 Rows, 6 Columns, UTF-8 인코딩

# 환자의 상태와 그에 따라 처방된 약에 대한 정보를 분석하고자한다
# 
# 컬 럼 / 정 의  / Type
# Age  / 연령 / Integer
# Sex / 성별 / String
# BP / 혈압 레벨 / String
# Cholesterol / 콜레스테롤 레벨 /  String
# Na_to_k / 혈액 내 칼륨에 대비한 나트륨 비율 / Double
# Drug / Drug Type / String
# =============================================================================
# =============================================================================

import pandas as pd
import numpy as np

data2 = pd.read_csv('/Users/kij/workspace/20220421_ProDS/Dataset/Dataset_02.csv')
data2.columns
# ['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K', 'Drug']

#%%

# =============================================================================
# 1.해당 데이터에 대한 EDA를 수행하고, 여성으로 혈압이 High, Cholesterol이 Normal인
# 환자의 전체에 대비한 비율이 얼마인지 소수점 네 번째 자리에서 반올림하여 소수점 셋째
# 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================
q1 = data2[['Sex', 'BP', 'Cholesterol']].value_counts(normalize=True)
q1.index
q1[('F', 'HIGH', 'NORMAL')]

# 답: 0.105

#%%

# =============================================================================
# 2. Age, Sex, BP, Cholesterol 및 Na_to_k 값이 Drug 타입에 영향을 미치는지 확인하기
# 위하여 아래와 같이 데이터를 변환하고 분석을 수행하시오. 
# - Age_gr 컬럼을 만들고, Age가 20 미만은 ‘10’, 20부터 30 미만은 ‘20’, 30부터 40 미만은
# ‘30’, 40부터 50 미만은 ‘40’, 50부터 60 미만은 ‘50’, 60이상은 ‘60’으로 변환하시오. 
# - Na_K_gr 컬럼을 만들고 Na_to_k 값이 10이하는 ‘Lv1’, 20이하는 ‘Lv2’, 30이하는 ‘Lv3’, 30 
# 초과는 ‘Lv4’로 변환하시오.
# - Sex, BP, Cholesterol, Age_gr, Na_K_gr이 Drug 변수와 영향이 있는지 독립성 검정을
# 수행하시오.
# - 검정 수행 결과, Drug 타입과 연관성이 있는 변수는 몇 개인가? 연관성이 있는 변수
# 가운데 가장 큰 p-value를 찾아 소수점 여섯 번째 자리 이하는 버리고 소수점 다섯
# 번째 자리까지 기술하시오.
# (답안 예시) 3, 1.23456
# =============================================================================

# 1. 변수 생성
q2 = data2.copy()
# np.where(조건)
# np.where(조건[True/False]), 참인 경우 실행[함수(식), 상수, 시리즈], 거짓인 경우 실행)

q2['Age_gr'] = np.where(q2['Age'] < 20, 10,
                np.where(q2['Age'] < 30, 20,
                np.where(q2['Age'] < 40, 30,
                np.where(q2['Age'] < 50, 40,
                np.where(q2['Age'] < 60, 50, 60)))))


q2['Na_K_gr'] = np.where(q2['Na_to_K'] <= 10, 'Lv1',
                np.where(q2['Na_to_K'] <= 20, 'Lv2',
                np.where(q2['Na_to_K'] <= 30, 'Lv3', 'Lv4')))

# 2. 반복적 카이스퀘어 검정
# - 반복적 두 변수간의 카이스퀘어 검정
# - 반복적으로 사용할 변수 목록
# - for 루프 안에서 카이스퀘어 검정이 진행(입력값은 빈도표로 들어가도록 설계)

from scipy.stats import chi2_contingency

var_list = ['Sex', 'BP', 'Cholesterol', 'Age_gr', 'Na_K_gr']

q2_out = []
for i in var_list:
    # tab = pd.crosstab(index = q2['Sex'], columns = q2['Drug'])
    tab = pd.crosstab(index = q2[i], columns = q2['Drug'])
    chi_out = chi2_contingency(tab)
    pvalue = chi_out[1]
    q2_out.append([i, pvalue])

q2_out = pd.DataFrame(q2_out,columns=['var', 'pvalue'])

q2_out[q2_out.pvalue < 0.05]
(q2_out.pvalue < 0.05).sum()
len(q2_out[q2_out.pvalue < 0.05])

q2_out2 = q2_out[q2_out.pvalue < 0.05]
q2_out2.pvalue.max()
# 답 : 4, 0.00070

# [참고]
# H0 : 두 변수는 독립이다
# H1 : 두 변수는 독립이 아니다(상관이 있다)
# 평가 : 유의수준 체크
# 유의수준 0.05 하에서 p-value가 유의수준보다 작은지 확인, 유의수준보다 작으면 귀무가설 기각,
# 즉, 상관이 있다는 의미

#%%

# =============================================================================
# 3.Sex, BP, Cholesterol 등 세 개의 변수를 다음과 같이 변환하고 의사결정나무를 이용한
# 분석을 수행하시오.
# - Sex는 M을 0, F를 1로 변환하여 Sex_cd 변수 생성
# - BP는 LOW는 0, NORMAL은 1 그리고 HIGH는 2로 변환하여 BP_cd 변수 생성
# - Cholesterol은 NORMAL은 0, HIGH는 1로 변환하여 Ch_cd 생성
# - Age, Na_to_k, Sex_cd, BP_cd, Ch_cd를 Feature로, Drug을 Label로 하여 의사결정나무를
# 수행하고 Root Node의 split feature와 split value를 기술하시오. 
# 이 때 split value는 소수점 셋째 자리까지 반올림하여 기술하시오. (답안 예시) Age, 
# 12.345
# =============================================================================

# 1. 변수 변환
q3 = data2.copy()
q3['Sex_cd'] = np.where(q3.Sex =='M', 0, 1)
q3['BP_cd'] = np.where(q3.BP == 'LOW', 0, 
            np.where(q3.BP == 'NORMAL', 1, 2))
q3['Ch_cd'] = np.where(q3.Cholesterol == 'NORMAL', 0, 1)

# 2. 의사결정나무 수행
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text

var_list = ['Age', 'Na_to_K', 'Sex_cd', 'BP_cd', 'Ch_cd']

dt = DecisionTreeClassifier().fit(q3[var_list], q3['Drug'])

plot_tree(dt, max_depth=2, feature_names=var_list, 
          class_names=list(q3.Drug.unique()),
          precision=3, fontsize=7)

print(export_text(dt, feature_names=var_list, decimals=3))

# 답: Na_to_K, 14.829


#%%

# =============================================================================
# =============================================================================
# # 문제 03 유형(DataSet_03.csv 이용)
# 
# 구분자 : comma(“,”), 5,001 Rows, 8 Columns, UTF-8 인코딩
# 안경 체인을 운영하고 있는 한 회사에서 고객 사진을 바탕으로 안경의 사이즈를
# 맞춤 제작하는 비즈니스를 기획하고 있다. 우선 데이터만으로 고객의 성별을
# 파악하는 것이 가능할 지를 연구하고자 한다.
#
# 컬 럼 / 정 의 / Type
# long_hair / 머리카락 길이 (0 – 길지 않은 경우 / 1 – 긴
# 경우) / Integer
# forehead_width_cm / 이마의 폭 (cm) / Double
# forehead_height_cm / 이마의 높이 (cm) / Double
# nose_wide / 코의 넓이 (0 – 넓지 않은 경우 / 1 – 넓은 경우) / Integer
# nose_long / 코의 길이 (0 – 길지 않은 경우 / 1 – 긴 경우) / Integer
# lips_thin / 입술이 얇은지 여부 0 – 얇지 않은 경우 / 1 –
# 얇은 경우) / Integer
# distance_nose_to_lip_long / 인중의 길이(0 – 인중이 짧은 경우 / 1 – 인중이
# 긴 경우) / Integer
# gender / 성별 (Female / Male) / String
# =============================================================================
# =============================================================================

import pandas as pd
import numpy as np

data3 = pd.read_csv('/Users/kij/workspace/20220421_ProDS/Dataset/Dataset_03.csv')
data3.columns
# ['long_hair', 'forehead_width_cm', 'forehead_height_cm', 'nose_wide',
#   'nose_long', 'lips_thin', 'distance_nose_to_lip_long', 'gender']
#%%

# =============================================================================
# 1.이마의 폭(forehead_width_cm)과 높이(forehead_height_cm) 사이의
# 비율(forehead_ratio)에 대해서 평균으로부터 3 표준편차 밖의 경우를 이상치로
# 정의할 때, 이상치에 해당하는 데이터는 몇 개인가? (답안 예시) 10
# =============================================================================

q1 = data3.copy()
q1['forehead_ratio'] = q1['forehead_width_cm'] / q1['forehead_height_cm']

xbar = q1['forehead_ratio'].mean()
std = q1['forehead_ratio'].std()

# 이상치 판정 구간, 하한(LB), 상한(UB)
LB = xbar - (3 * std)
UB = xbar + (3 * std)

# 이상치 판정
len(q1[(q1['forehead_ratio'] < LB) | (q1['forehead_ratio'] > UB)]) # | == or

# 답: 3

#%%

# =============================================================================
# 2.성별에 따라 forehead_ratio 평균에 차이가 있는지 적절한 통계 검정을 수행하시오.
# - 검정은 이분산을 가정하고 수행한다.
# - 검정통계량의 추정치는 절대값을 취한 후 소수점 셋째 자리까지 반올림하여
# 기술하시오.
# - 신뢰수준 99%에서 양측 검정을 수행하고 결과는 귀무가설 기각의 경우 Y로, 그렇지
# 않을 경우 N으로 답하시오. (답안 예시) 1.234, Y
# =============================================================================

# [단일 모집단] -> 단일 표본
# 1. 일표본 t 검정: ttest_1samp

# [복수 모집단] - 각 모집단별로 표본 추출
# 1. 표본의 수가 2개인 경우:
# (1) 독립인 이표본 t 검정: ttest_ind
# (2) 대응인 이표본 t 검정: ttest_rel

# 2. 표본의 수가 3개 이상인 경우 : 분산분석(ANOVA)

# H0: 성별 간에 평균 차이가 없다 mu(남) == mu(여) => mu(남) - mu(여) = 0
# H1: 성별 간에 평균 차이가 있다 mu(남) != mu(여)

gr_m = q1[q1.gender == 'Male']['forehead_ratio']
gr_f = q1[q1.gender == 'Female']['forehead_ratio']

from scipy.stats import ttest_ind, bartlett, levene

# 1. 등분산검정 수행 => 이분산을 가정하고 수행 생략

bartlett(gr_m, gr_f)
# H0: 등분산이다
# H1: 이분산이다
# => 결론: 이분산

# 2. ttest 수행
q2_out = ttest_ind(gr_m, gr_f, equal_var=False)

# 3. 판정 : 유의수준 확인 (신뢰수준 99% -> 0.01)
dir(q2_out)

# 검정통계량의 추정치는 절대값을 취한 후 소수점 셋째 자리까지 반올림하여 기술
round(abs(q2_out.statistic), 3) # 2.999

# 신뢰수준 99%에서 양측 검정을 수행하고 결과는 귀무가설 기각의 경우 Y로, 그렇지
# 않을 경우 N으로 답
q2_out.pvalue < 0.01 # Y

# 답: 2.999, Y

#%%

# =============================================================================
# 3.주어진 데이터를 사용하여 성별을 구분할 수 있는지 로지스틱 회귀분석을 적용하여
# 알아 보고자 한다. 
# - 데이터를 7대 3으로 나누어 각각 Train과 Test set로 사용한다. 이 때 seed는 123으로
# 한다.
# - 원 데이터에 있는 7개의 변수만 Feature로 사용하고 gender를 label로 사용한다.
# (forehead_ratio는 사용하지 않음)
# - 로지스틱 회귀분석 예측 함수와 Test dataset를 사용하여 예측을 수행하고 정확도를
# 평가한다. 이 때 임계값은 0.5를 사용한다. 
# - Male의 Precision 값을 소수점 둘째 자리까지 반올림하여 기술하시오. (답안 예시) 
# 0.12
# 
# 
# (참고) 
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn import metrics
# train_test_split 의 random_state = 123
# =============================================================================

# 1. 데이터를 7대 3으로 나누어 각각 Train과 Test set로 사용(seed는 123)

from sklearn.model_selection import train_test_split

train, test = train_test_split(data3, test_size=0.3, random_state=123)

# 2. 입력 변수 선정
var_list = train.columns.drop('gender')

# 3. Test dataset를 사용하여 예측을 수행하고 정확도를
# 평가한다. 이 때 임계값은 0.5를 사용한다.
# Male의 Precision 값을 소수점 둘째 자리까지 반올림하여 기술

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, classification_report

logit = LogisticRegression().fit(train[var_list], train['gender'])
pred_class = logit.predict(test[var_list])
pred_pr = logit.predict_proba(test[var_list])

# 임계값이 0.8인 경우
pred_class2 = np.where(pred_pr[:,1] >= 0.8, 'Male')

round(precision_score(test['gender'], pred_class, pos_label='Male'), 2)

# 답: 0.96

print(round(classification_report(test['gender'], pred_class))

#%%

# =============================================================================
# =============================================================================
# # 문제 04 유형(DataSet_04.csv 이용)
#
#구분자 : comma(“,”), 6,718 Rows, 4 Columns, UTF-8 인코딩

# 한국인의 식생활 변화가 건강에 미치는 영향을 분석하기에 앞서 육류
# 소비량에 대한 분석을 하려고 한다. 확보한 데이터는 세계 각국의 1인당
# 육류 소비량 데이터로 아래와 같은 내용을 담고 있다.

# 컬 럼 / 정 의 / Type
# LOCATION / 국가명 / String
# SUBJECT / 육류 종류 (BEEF / PIG / POULTRY / SHEEP) / String
# TIME / 연도 (1990 ~ 2026) / Integer
# Value / 1인당 육류 소비량 (KG) / Double
# =============================================================================
# =============================================================================

# (참고)
# #1
# import pandas as pd
# import numpy as np
# #2
# from scipy.stats import ttest_rel
# #3
# from sklearn.linear_model import LinearRegression

#%%

import pandas as pd
import numpy as np

data4 = pd.read_csv('/Users/kij/workspace/20220421_ProDS/Dataset/Dataset_04.csv')
data4.columns

# ['LOCATION', 'SUBJECT', 'TIME', 'Value']

# =============================================================================
# 1.한국인의 1인당 육류 소비량이 해가 갈수록 증가하는 것으로 보여 상관분석을 통하여
# 확인하려고 한다. 
# - 데이터 파일로부터 한국 데이터만 추출한다. 한국은 KOR로 표기되어 있다.
# - 년도별 육류 소비량 합계를 구하여 TIME과 Value간의 상관분석을 수행하고
# 상관계수를 소수점 셋째 자리에서 반올림하여 소수점 둘째 자리까지만 기술하시오. 
# (답안 예시) 0.55
# =============================================================================

# 1. 데이터 파일로부터 한국 데이터만 추출
q1 = data4[data4.LOCATION == 'KOR']

# 2. 년도별 육류 소비량 합계
tab = q1.groupby('TIME')['Value'].sum().reset_index()

# 3. TIME과 Value간의 상관분석을 수행
round(tab.corr()['TIME']['Value'], 2)

# 답: 0.96

#%%

# =============================================================================
# 2. 한국 인근 국가 가운데 식생의 유사성이 상대적으로 높은 일본(JPN)과 비교하여, 연도별
# 소비량에 평균 차이가 있는지 분석하고자 한다.
# - 두 국가의 육류별 소비량을 연도기준으로 비교하는 대응표본 t 검정을 수행하시오.
# - 두 국가 간의 연도별 소비량 차이가 없는 것으로 판단할 수 있는 육류 종류를 모두
# 적으시오. (알파벳 순서) (답안 예시) BEEF, PIG, POULTRY, SHEEP
# =============================================================================

# 1. 한국, 일본 데이터 필터링
q2 = data4[data4.LOCATION.isin(['KOR', 'JPN'])]

# 2. 육류 종류 추출
sub_list = q2.SUBJECT.unique()
# ['BEEF', 'PIG', 'POULTRY', 'SHEEP']

# 3. 육류 종류별로 연도를 기준으로 쌍이 되도록 데이터를 설계
# 4. 육류 종류별로 대응 t 검정 수행(pvalue 수집 -> 육류 종류 도출)
# 귀무가설을 기각하지 않는
from scipy.stats import ttest_rel

q2
for i in sub_list:
    temp = q2[q2.SUBJECT == i]
    tab = pd.pivot_table(temp, index='TIME', 
                         columns='LOCATION',
                         values='Value',
                         aggfunc='mean').dropna()
    ttest_out = ttest_rel(tab['KOR'], tab['JPN'])
    pvalue = ttest_out.pvalue
    q2_out.append([i, pvalue])
    
# 5. 연도별 소비량 차이가 없는 것으로 판단할 수 있는 육류 종류
    

# [참고]
temp = q2[q2.SUBJECT == 'BEEF']
tab = pd.pivot_table(temp, index='TIME',
                     columns='LOCATION',
                     values='Value',
                     aggfunc='mean').dropna()



#%%

# =============================================================================
# 3.(한국만 포함한 데이터에서) Time을 독립변수로, Value를 종속변수로 하여 육류
# 종류(SUBJECT) 별로 회귀분석을 수행하였을 때, 가장 높은 결정계수를 가진 모델의
# 학습오차 중 MAPE를 반올림하여 소수점 둘째 자리까지 기술하시오. (답안 예시) 21.12
# (MAPE : Mean Absolute Percentage Error, 평균 절대 백분율 오차)
# (MAPE = Σ ( | y - y ̂ | / y ) * 100/n ))
# 
# =============================================================================

# 1. 한국만 포함한 데이터에서
q3 = data4[data4.LOCATION == 'KOR']

# 2. 육류 종류
sub_list = q3.SUBJECT.unique()

# 3. 육류 종류별로 회귀분석
# - 반복문, 결정계수, MAPE
from sklearn.linear_model import LinearRegression

q3_out = []
for i in sub_list:
    temp = q3[q3.SUBJECT == i]
    lm = LinearRegression().fit(temp[['TIME']], temp['Value']) # 입력 데이터 dim이 2차
    r2 = lm.score(temp[['TIME']], temp['Value'])
    # MAPE = = Σ ( | y - y ̂ | / y ) * 100/n 
    pred = lm.predict(temp[['TIME']])
    mape = (abs(temp['Value'] - pred) / temp['Value']).sum() * 100 / len(temp)    
    q3_out.append([i, r2, mape])
    
# 4. 가장 높은 결정계수를 가진 모델의
# 학습오차 중 MAPE를 반올림하여 소수점 둘째 자리까지 기술

q3_out = pd.DataFrame(q3_out, columns=['sub', 'r2', 'mape'])

round(q3_out.loc[q3_out.r2.idxmax(), 'mape'], 2)

# 답: 5.78
    
# [참고]
temp['TIME'].ndim
temp['TIME'].shape
temp[['TIME']].ndim
temp[['TIME']].shape


#%%

# =============================================================================
# =============================================================================
# # 문제 05 유형(DataSet_05.csv 이용)
#
# 구분자 : comma(“,”), 8,068 Rows, 12 Columns, UTF-8 인코딩
#
# A자동차 회사는 신규 진입하는 시장에 기존 모델을 판매하기 위한 마케팅 전략을 
# 세우려고 한다. 기존 시장과 고객 특성이 유사하다는 전제 하에 기존 고객을 세분화하여
# 각 그룹의 특징을 파악하고, 이를 이용하여 신규 진입 시장의 마케팅 계획을 
# 수립하고자 한다. 다음은 기존 시장 고객에 대한 데이터이다.
#

# 컬 럼 / 정 의 / Type
# ID / 고유 식별자 / Double
# Age / 나이 / Double
# Age_gr / 나이 그룹 (10/20/30/40/50/60/70) / Double
# Gender / 성별 (여성 : 0 / 남성 : 1) / Double
# Work_Experience / 취업 연수 (0 ~ 14) / Double
# Family_Size / 가족 규모 (1 ~ 9) / Double
# Ever_Married / 결혼 여부 (Unknown : 0 / No : 1 / Yes : 2) / Double
# Graduated / 재학 중인지 여부 / Double
# Profession / 직업 (Unknown : 0 / Artist ~ Marketing 등 9개) / Double
# Spending_Score / 소비 점수 (Average : 0 / High : 1 / Low : 2) / Double
# Var_1 / 내용이 알려지지 않은 고객 분류 코드 (0 ~ 7) / Double
# Segmentation / 고객 세분화 결과 (A ~ D) / String
# =============================================================================
# =============================================================================


#(참고)
#1
# import pandas as pd
# #2
# from scipy.stats import chi2_contingency
# #3
# from sklearn.model_selection import train_test_split
# from sklearn import metrics
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.tree import export_graphviz
# import pydot


#%%

import pandas as pd
import numpy as np

data5 = pd.read_csv('/Users/kij/workspace/20220421_ProDS/Dataset/Dataset_05.csv')
data5.columns
# ['ID', 'Age', 'Age_gr', 'Gender', 'Work_Experience', 'Family_Size',
#       'Ever_Married', 'Graduated', 'Profession', 'Spending_Score', 'Var_1',
#       'Segmentation']

# =============================================================================
# 1.위의 표에 표시된 데이터 타입에 맞도록 전처리를 수행하였을 때, 데이터 파일 내에
# 존재하는 결측값은 모두 몇 개인가? 숫자형 데이터와 문자열 데이터의 결측값을
# 모두 더하여 답하시오.
# (String 타입 변수의 경우 White Space(Blank)를 결측으로 처리한다) (답안 예시) 123
# =============================================================================

data5.isna().sum().sum()

# 답: 1166


#%%

# =============================================================================
# 2.이어지는 분석을 위해 결측값을 모두 삭제한다. 그리고, 성별이 세분화(Segmentation)에
# 영향을 미치는지 독립성 검정을 수행한다. 수행 결과, p-value를 반올림하여 소수점
# 넷째 자리까지 쓰고, 귀무가설을 기각하면 Y로, 기각할 수 없으면 N으로 기술하시오. 
# (답안 예시) 0.2345, N
# =============================================================================

q2 = data5.dropna()

tab =pd.crosstab(index=q2['Gender'], columns=q2['Segmentation'])

from scipy.stats import chi2_contingency

chi2_out = chi2_contingency(tab)

round(chi2_out[1], 4)

# 답: 0.0031, Y


#%%

# =============================================================================
# 3.Segmentation 값이 A 또는 D인 데이터만 사용하여 의사결정 나무 기법으로 분류
# 정확도를
# 측정해 본다. 
# - 결측치가 포함된 행은 제거한 후 진행하시오.
# - Train대 Test 7대3으로 데이터를 분리한다. (Seed = 123)
# - Train 데이터를 사용하여 의사결정나무 학습을 수행하고, Test 데이터로 평가를
# 수행한다.
# - 의사결정나무 학습 시, 다음과 같이 설정하시오:
# • Feature: Age_gr, Gender, Work_Experience, Family_Size, 
#             Ever_Married, Graduated, Spending_Score
# • Label : Segmentation
# • Parameter : Gini / Max Depth = 7 / Seed = 123
# 이 때 전체 정확도(Accuracy)를 소수점 셋째 자리 이하는 버리고 소수점 둘째자리까지
# 기술하시오.
# (답안 예시) 0.12
# =============================================================================

# Segmentation 값이 A 또는 D인 데이터만 사용
q3 = q2[q2.Segmentation.isin(['A', 'D'])]

from sklearn.model_selection import train_test_split

# Train대 Test 7대3으로 데이터를 분리한다. (Seed = 123)
train, test = train_test_split(q3, test_size=0.3, random_state=123)

# 의사결정나무 학습
from sklearn.tree import DecisionTreeClassifier

var_list = ['Age_gr', 'Gender', 'Work_Experience', 'Family_Size', 
             'Ever_Married', 'Graduated', 'Spending_Score']

dt = DecisionTreeClassifier(max_depth=7, random_state=123)
dt.fit(train[var_list], train['Sefmentation'])

# Test 데이터로 평가를     
# 전체 정확도(Accuracy)를 소수점 셋째 자리 이하는 버리고 소수점 둘째자리까지
# 기술      
dt.score(test[var_list], test['Segmentation'])     
  
# 답: 0.68









