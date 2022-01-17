#main.py
#import mod1
#from mod1 import *
from mod1 import add, sub #추천
#import mod.mod2 as mod2 #파일 지정

import sys
sys.path.append('/Users/kij/workspace/220117/mod')
print(sys.path)
import mod2


# 임포트 형식
# import 모듈명
#from 모듈명 import 함수명, 변수

#print(mod1.add(3, 4))
#print(mod1.sub(4, 2))

print(add(3, 4))
print(sub(4, 2))

print(mod2.PI)

#mod2파일의 Math1클래스를 사용하기 위해 선언한다
a = mod2.Math1() #객체를 만듬
print(a.solv(2))

result = a.add(mod2.PI, 2)
print(result)
print(a.add(mod2.PI, 2))

result1 = mod2.add1(mod2.PI, 2)
print(result1)