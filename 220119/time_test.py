import time

# # Epoch time
# print(time.time())

# 시간 변환
# print(time.localtime(time.time()))
# time.struct_time(tm_year=2022, tm_mon=1, tm_mday=19, tm_hour=10, tm_min=52, tm_sec=0, tm_wday=2, tm_yday=19, tm_isdst=0)

# 시간 변환
# print(time.asctime(time.localtime(time.time())))
# Wed Jan 19 10:52:19 2022

# print(time.ctime())
# Wed Jan 19 10:52:39 2022

# 시간 포맷
print(time.strftime('%x', time.localtime(time.time())))
# 01/19/22
print(time.strftime('%c', time.localtime(time.time())))
# Wed Jan 19 10:54:46 2022