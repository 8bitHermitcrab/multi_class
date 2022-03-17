# 팰린드롬


def find_palindrome(k, words):
    for i in range(k - 1):
        for j in range(i + 1, k):
            password1 = words[i] + words[j]
            if password1 == password1[::-1]:
                return password1
            
            password2 = words[j] + words[i]
            if password2 == password2[::-1]:
                return password2
    return 0


for _ in range(int(input())):
    k = int(input())
    words = [input() for _ in range(k)]
    print(find_palindrome(k, words))


    # k * kT
    # if k == k[::-1]:
    #     print(k)
    # else:
    #     print('0')