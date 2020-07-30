# -*- coding: utf-8 -*-
'''模块、类和对象
使用类而不用模块的原因有：你可以用这个 MyStuff 类复制很多个，如果你想的话，一次几百万个都行，并且它们之间不会相互干涉。但是当你导入一个模块，对整个程序来说只有一个。
如果说类是一个小型模块，那么应该要有一个概念和 import 类似。这个概念就叫做“实例化”（instantiate）。当你实例化一个类，你得到的东西就叫做对象。
'''


class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


thing = MyStuff()
thing.apple()
print(thing.tangerine)
