# 나무 조각

# 버블 정렬

nums = list(map(int, input().split()))
n = len(nums)

for i in range(n-1):
    for j in range(n-i-1):
        # print(f'i = {i}, j = {j}, n-i-1 = {n-i-1}')
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            print(' '.join(map(str, nums)))

# for i in range(n):
#     print('%d'%nums[i], end='')