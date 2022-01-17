#mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print(__name__)

if __name__ == '__main__':
    print('=========', add(3, 5))
    print('=========', sub(5, 2))
