# 나는 요리사다

nums = [list(map(int, input().split())) for _ in range(5)]
score = [sum(num) for num in nums]

print(score.index(max(score))+1, max(score))
