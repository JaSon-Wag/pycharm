class Instrument:
    def make_sound(self):
        pass


class Erch(Instrument):
    def make_sound(self):
        print('二胡在弹奏')


class Piano(Instrument):
    def make_sound(self):
        print('钢琴在演奏')


class Violin(Instrument):
    def make_sound(self):
        print('小提琴在演奏')


# 编写一个函数
def play(obj):
    obj.make_sound()


# 创建对象
er = Erch()
piano = Piano()
vio = Violin()

# 调用方法
play(er)
play(piano)
play(vio)
