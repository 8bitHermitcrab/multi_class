# 오타맨 고창영

T = int(input())

for i in range(T):
    index, word = input().split()
    index = int(index)
    print(word[:index-1] + word[index:])


'''
문자열   index   문자열
1~3     4x      5~

for _ in range(int(input())):
    index, word = input().split()
# int("4") "MISSSPELL"
    index = int(index)
    print(word[:index-1] + word[index:])
'''