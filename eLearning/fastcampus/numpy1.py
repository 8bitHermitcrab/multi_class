import numpy as np

# replace = False : 비복원 추출(중복값 제거)
def generate_lotto_nums():
    return np.random.choice(np.arange(1, 46), size=6, replace=False)

print(generate_lotto_nums())