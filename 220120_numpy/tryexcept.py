# 1. 객체화 : 옷 구매
class MyError(Exception):
    #print('바보라고 부르지마')
    # def __str__(self) -> str :
    #     super().__str__()
    #     return '바보라고 부르지마'
    pass


# 2. 옷 입기
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    else :
        print(nick)


try:
    say_nick('바부')
    # say_nick('바보')

except Exception as e :
    print(e)