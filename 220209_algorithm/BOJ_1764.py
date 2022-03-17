# 듣보잡
N, M = map(int, input().split())

a = {input() for _ in range(N)}
b = {input() for _ in range(M)}

# print(f'a = {a}')
# print(f'b = {b}')
# print(f'list(a & b) = {list(a & b)}')
# result = sorted(list(a & b))
# print(f'result = {result}')
result = sorted(a & b)
print(len(result))

for i in result:
    print(i)


'''
N, M = map(int, input().split())

a = set()
b = set()

for i in range(N):
    a.add(input())

for i in range(M):
    b.add(input())

# print(f'a = {a}')
# print(f'b = {b}')
# print(f'list(a & b) = {list(a & b)}')
result = sorted(list(a & b))
# print(f'result = {result}')
print(len(result))

for i in result:
    print(i)
'''

'''
# n_value = [input() for _ in range(N)]
# m_value = [input() for _ in range(M)]

# nm = n_value + m_value

# 중복값 제거
nm_set = set(nm)
nm_del = list(nm_set)

# print(len(nm)-len(nm_del))

print(nm - nm_del)

https://wook-2124.tistory.com/476
'''
