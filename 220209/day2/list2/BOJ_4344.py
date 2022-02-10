# 평균은 넘겠지

n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    # nums[1:] = 학생들 점수, nums[0] = 학생들 과목수
    avg = sum(nums[1:])/nums[0]
    avg_num = 0
    for score in nums[1:]: 
        if score > avg:
            # 평균 이상인 학생 수
            avg_num += 1
            # print(avg_num)

    rate = avg_num/nums[0] * 100
    print(f'{rate:.3f}%')