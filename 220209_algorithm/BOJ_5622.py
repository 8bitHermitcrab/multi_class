# 다이얼

# 1에 2초 
'''
2ABC는 +1초 = 3초
3DEF 4
4GHI 5
5JKL 6
6MNO 7
7PQRS 8
8TUV 9
9WXYZ 10
0 11
'''

dial = {'A':3, 'B':3, 'C':3, 
'D':4, 'E':4, 'F':4,
'G':5, 'H':5, 'I':5,
'J':6, 'K':6, 'L':6,
'M':7, 'N':7, 'O':7,
'P':8, 'Q':8, 'R':8, 'S':8,
'T':9, 'U':9, 'V':9,
'W':10, 'X':10, 'Y':10, 'Z':10}

word = input().upper()

#print(word[0])
count = 0  

for i in range(len(word)):
    for key in dial:
        if word[i] == key:
            count = count + dial[key]

print(count)

'''
https://j-remind.tistory.com/76
'''