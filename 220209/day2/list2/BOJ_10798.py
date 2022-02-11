# 세로 읽기

word = [input() for _ in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(word[j]):
            print(word[j][i], end='')
            

#     sero_word.append(w)
# print(sero_word)
# print(*sero_word)