# 유학 금지

word = input()
word = word.upper()
for i in 'CAMBRIDGE':
    word = word.replace(i, '')
print(word)