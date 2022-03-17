# 리스트3 - 자가진단 7

# 5명 학생, 4과목
# 평균 >= 80 -> pass
# 평균 < 80 -> fail

# i : 0~4
# j : 0~3

# 합격자수 += 1


score = [list(map(int, input().split())) for _ in range(5)]
success = 0


for i in range(5):
    total = 0
    for j in range(4):
        total += score[i][j]
    # print(total)
    average = total/4
    if average >= 80:
        success += 1
        print("pass")
    else:
        print("fail")
print(f'Successful : {success}')



'''
for i in range(5):
    score = list(map(int, input().split()))
    avg = sum(score[:])/4
    avg_n = 0
    #print(avg)
for j in score[:]:
    if avg >= 80:
        print('pass')
        avg_n += 1
    else:
        print('fail')

print(f'Successful : {avg_n}')
'''
    
        # print(f'Successful : {count('pass')}')

'''
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
'''


""" if avg >= 80:
    print('pass')
else:
    print('fail') """