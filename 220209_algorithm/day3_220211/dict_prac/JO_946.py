# 기타 자료형 - 자가진단 6

n = int(input())
country = {}

for _ in range(n):
    nation, capital = input().split()
    country[nation] = capital

word = input()

print(country.get(word, 'Unknown Country'))
