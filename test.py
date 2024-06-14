# class Test():
#     def __init__(self, a: int, b: int, c: int):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_umnozenie(selfs):
#         return selfs.a * selfs.b * selfs.c
#
#
# t = Test(a=1, b=2, c=3)
# print(t.get_umnozenie())


class test_expamle():
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def get_slozenie(self):
        return self.a + self.b + self.c


g = test_expamle(4, 2, 3)

print(g.get_slozenie())
