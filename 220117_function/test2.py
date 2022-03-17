#test2.py

try:
    age = int(input('나이를 입력하세요. : '))
#else문
    if age < 18:
        print('미성년자')
    else:
        print('환영합니다.')

except Exception as e:
    print('입력이 정확하지 않습니다. : ', e)


"""
#else문 
else:
    if age < 18:
        print('미성년자')
    else:
        print('환영합니다.') 
"""