class test_forp():
    def __init__(self,slide_a, slide_b):
        self.slide_a = slide_a
        self.slide_b = slide_b

    def get_perimeter(self):
        if self.slide_a == self.slide_b or self.slide_a < 0 or self.slide_b < 0:
           return ValueError('Error = or negative')
        return (self.slide_a + self.slide_b) *2


s = test_forp(-3,5)
print(s.get_perimeter())