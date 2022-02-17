# 나는야 포켓몬 마스터 이다솜

# 도감과 찾을 개수 입력
# 포켓몬 리스트에서 같은 이름을 찾거나 인덱스+1의 숫자를 출력한다.

'''
pokemon = {'1':'Bulbasaur', '2':'Ivysaur', '3':'Venusaur', '4':'Charmander', '5':'Charmeleon', 
'6':'Charizard', '7':'Squirtle', '8': 'Wartortle', '9':'Blastoise', '10':'Caterpie', '11':'Metapod', 
'12':'Butterfree', '13':'Weedle', '14':'Kakuna', '15':'Beedrill', '16':'Pidgey', '17':'Pidgeotto', 
'18':'Pidgeot', '19':'Rattata', '20':'Raticate', '21':'Raticate', '22':'Spearow', '23':'Fearow', 
'24':'Ekans', '25':'Ekans', '26':'Arbok', '27':'Pikachu', '28':'Raichu'}
'''

pokemon = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 
'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 
'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Raticate', 'Spearow', 'Fearow', 
'Ekans', 'Ekans', 'Arbok', 'Pikachu', 'Raichu']

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 포켓몬을 저장할 딕셔너리
pokemon_dogam = {}

for i in range(1, n + 1):
    a = input().rstrip()
    pokemon_dogam[i] = a
    pokemon_dogam[a] = i

for i in range(m):
    pokemon_info = input().rstrip()
    # 숫자가 왔을 때, 정보를 숫자로 바꿔서 포켓몬 이름을 출력
    if pokemon_info.isdigit():
        print(pokemon_dogam[int(pokemon_info)])
    # 문자가 왔을 때, 딕셔너리의 value값을 출력
    else:
        print(pokemon_dogam[pokemon_info])


""" 
for i in range(m):
    pokemon_info = input().rstrip()
    # 숫자가 왔을 때, 도감숫자의 -1을 해서 포켓몬 이름 리스트의 인덱스값을 넣고 포켓몬 이름을 출력
    if pokemon_info.isdifit():
        print(pokemon_name[int(pokemon_info)-1])
    # 문자가 왔을 때, 딕셔너리의 value값을 출력
    else:
        print(pokemon_dogam[pokemon_info])

for i in range(dogam):
    for key, value in pokemon.items():
    # 만약 이름이 왔다면
        if name == value:
            # 포켓몬 번호 리스트
            a = pokemon.keys()
            b = a[i]
            print()
    # 숫자가 왔다면
        elif name == key:
            # 포켓몬 이름 리스트
            a = pokemon.values()
            b = a[]
            print(b) 


     https://gudwns1243.tistory.com/63
"""