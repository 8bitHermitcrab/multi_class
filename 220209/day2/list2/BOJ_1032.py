# 명령 프롬프트

N = int(input())
file_name = list(input())
file_num = len(file_name)

for i in range(N - 1):
    file_name2 = list(input())
    for j in range(file_num):
        if file_name[j] != file_name2[j]:
            file_name[j] = '?'

print(''.join(file_name))

""" 
for name in file_name: # 리스트 요소
    if N == 1:
        print(name)
    for n in name: # 리스트 요소의 1글자
        #print(n)
        for i in range(len(name)):
        #print(i)
            if name[n][i] != name[n][i+1]:
                name[n][i] = '?'
               print(name[n][:i] + name[n][i:])
            else : 
"""
            



# 다른 부분만 ? 출력한다.

# 모두 같으면 원본 그대로 출력한다.

# 아무것도 같지 않으면 ?를 출력한다.

# 패턴을 출력한다.