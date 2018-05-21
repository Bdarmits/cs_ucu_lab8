class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a = "dupa"):
        super().__init__(a)


qwe = A("heello")
wer = B
print(wer().a)
