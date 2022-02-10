# 세로 읽기


word = [list(map(str, input())) for _ in range(5)]
len_word = len(word)
sero_word = ''

for i in range(len_word):
    for j in range(len_word):
        w = word[j][i]
        sero_word += word[j][i]
        
print(sero_word)



#     sero_word.append(w)
# print(sero_word)
# print(*sero_word)