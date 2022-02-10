""" a = [1, 2]
b = a
b[0] = 3
print(a) """


a = [1, 2]
b = a[:] # 슬라이싱으로 복사
b[0] = 3
print(a)

numbers = [i for i in range(5)]
numbers = [i for i in range(0, 10, 2)]
numbers = [i*2 for i in range(10)]


