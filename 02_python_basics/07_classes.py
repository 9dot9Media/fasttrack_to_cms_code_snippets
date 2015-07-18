class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return '{} + i{}'.format(self.real, self.imag)

    def add(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return Complex(real_sum, imag_sum)

# Testing the Complex class
c1 = Complex(3, 4)
print(c1)
c2 = Complex(5, 7)
print(c2)
c3 = c1.add(c2)
print(c3)

print('({}) + ({}) = {}'.format(c1, c2, c3))


class Complex2(Complex):
    def __init__(self, real=0, imag=0):
        super().__init__(real, imag)

    def conjugate(self):
        return Complex2(self.real, -self.imag)

# Testing the Complex2 class
c1 = Complex2(3, 4)
print(c1)
c2 = c1.conjugate()
print(c2)  # Note how ugly this looks, can you do something about it?

print('({}) is the conjugate of ({})'.format(c1, c2))
