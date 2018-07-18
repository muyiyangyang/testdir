#coding: utf-8

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("score must be a number")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = value


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def heigth(self):
        return self._heigth

    @heigth.setter
    def heigth(self, value):
        self._heigth = value

    @property
    def resolution(self):
        return 786432


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
