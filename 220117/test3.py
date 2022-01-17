#test3.py

# Exception 발생시키는 것!
class Bird:
    def fly(self):
        # raise NotImplementedError
        print('I can fly')

class Eagle(Bird):
    pass

eagle = Eagle()

eagle.fly()