#test.py
""" # '''도 주석 가능
import sys

#print(sys.path)

sys.path.append('/Users/kij/workspace/220117/mod')

print(sys.path)
"""

#FileNotFoundError: [Errno 2] No such file or directory: 'xxx.txt'
#f = open('xxx.txt', 'r')

#ZeroDivisionError: division by zero
#print(4/0)

#IndexError: list index out of range
#a = [1, 2, 3]
#print(a[4])

#에러가 나도 끝까지 실행(try, except)
from ast import Index


try:
    a = [1, 2, 3]
    print(a[4])
    4/0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)

# except (ZeroDivisionError, IndexError) as e:
#     print(e)

#Exception은 부모 클래스, ZeroDivisionError, IndexError는 자식 클래스
except Exception as e:
    print(e)

print('Hello World')