# 파일 복사
#import shutil

#shutil.copy('lib/pickle_test.txt', 'lib/pickle_test2.txt')

# 디렉토리에 있는 파일들의 리스트
import glob
print(glob.glob('/Users/kij/workspace/220119/lib'))

# 임시파일 만들어보기
import tempfile
f = tempfile.mkstemp()
print(f)