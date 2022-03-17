# 숫자 문자열과 영단어

# 딕셔너리와 문자열 메서드

# 영단어를 숫자로 바꿔주기
# 키값을 찾고 그대로 둔다
# 밸류값을 찾으면 키값으로 바꾼다

s = input()

numbers = {
    '0' : 'zero',
    '1' :'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine'
        }

for key, value in numbers.items():
    s = s.replace(value, key)

int(s)

"""

for number in numbers:
    s = s.replace(number, numbers[number])

"""
    
