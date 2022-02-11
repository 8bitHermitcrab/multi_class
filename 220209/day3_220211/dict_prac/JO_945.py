# 기타 자료형 - 자가진단 5

# 딕셔너리 만들기
animation = {
    'Pokemon':'Pikachu', 
    'Digimon':'Agumon', 
    'Yugioh':'Black Magician'
}

word = input()

print(animation.get(word, "I don't know"))


# 세 개중에 나오면 value/I don't know
'''
if word in animation:
    print(animation[word])
else:
    print("I don't know")
'''