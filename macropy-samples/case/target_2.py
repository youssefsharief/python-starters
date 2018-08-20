from macropy.case_classes import macros, case


@case
class Point(x, y):  #pylint: disable=undefined-variable
    def increase_x(self, val):
        self.x = self.x + val


p = Point(1, 2)
p.increase_x(5)

print(p.x)
