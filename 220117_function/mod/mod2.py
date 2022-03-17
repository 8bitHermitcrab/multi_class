#mod2.py

PI = 3.141592 #원주율

class Math1:    #클래스
    def solv(self, r): #원의 넓이
        return PI * (r ** 2)
    
    def add(self, a, b):
        return a + b

def add1(a, b): #일반 함수
    return a + b