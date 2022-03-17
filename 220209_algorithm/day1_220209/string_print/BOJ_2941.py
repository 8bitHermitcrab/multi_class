# 크로아티아 알파벳

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
T = input()

for i in croa:
    if i in T:
        T = T.replace(i, '*')
        # print(T)

print(len(T))