T = int(input())

for i in range(T):
    if i % 2 == 0:
        print('* ' *T)
    else:
        print(' *' *T)

'''
for i in range(n):
    print("* " * if i % 2 == 0 else " *" * n)


for i in range(n):
    # if i가 짝수면?
    if i % 2 == 0:
        print("* " * n)
    else:
        print(" *" * n)

'''

'''
    n = 2
    * *
     * *

    n = 3
    * * *
     * * *
    * * *

    for i in range(2):
        i 
        0 "* " *2
        1 " *" *2

    for i in range(3):
        i
        0 "* " *3
        1 " *" *3
        2 "* " *3
    
    짝수 : "* " * k
    홀수 : " *" * k
'''