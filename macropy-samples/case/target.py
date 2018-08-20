from macropy.case_classes import macros, case  


@case
class Point(x, y):  #pylint: disable=undefined-variable
    pass


p = Point(1, 2)
x, y = p

print(str(p))  # Point(1, 2)
print(p.x)    # 1
print(p.y)    # 2
print(Point(1, 2) == Point(1, 2))  # True
print(x, y)   # (1, 2)
