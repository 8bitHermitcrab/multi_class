# 크로스워드 만들기

# A 는 가로, B 는 세로
'''
1. A, B를 받고
2. B와 A의 요소가 첫번째 같은 인덱스를 찾는다.
3. B에 A를 붙인다.
'''

""" A, B = input().split()

for index, char in enumerate(A):
    B_index = B.find(char)
    if B_index != -1:  # ???
        A_index = index
        break

for index, char in enumerate(B):
    if index == B_index:
        print(A)
    else:
        print('.' * A_index + char + '.' * (len(A) - A_index - 1)) """








'''
A, B = input().split()

for i in range(len(A)):
    if A[i] in B:
        garo = i 
        sero = B.index(A[i])
        break

for i in range(len(B)):
    if i == sero:
        print(A)
    else:
        print('.' * garo  + B[i] + '.' * (len(A) - garo -1))
'''




        # if i != A.index(i):
        #     print(('.' * j) + i + ('.' * len(B)))
        #     print(A[::])
        # else:
        #     print('A[::] = ', A[::])

    