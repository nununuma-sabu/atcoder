import math


class ComplexNumber:
    # コンストラクタ
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # 複素数の加算
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    # 複素数の減算
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    # 複素数の乗算
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    # 複素数の除算
    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imag_part = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real_part, imag_part)

    # 複素数の絶対値
    def abs(self):
        return (self.real**2 + self.imag**2) ** 0.5

    # 複素数の偏角
    def arg(self):
        return math.atan2(self.imag, self.real)

    # 複素数のノルム
    def norm(self):
        return self.real**2 + self.imag**2

    # 複素数の共役
    def conj(self):
        return ComplexNumber(self.real, -self.imag)

    # 複素数のべき乗
    def __pow__(self, exponent):
        if exponent == 0:
            return ComplexNumber(1, 0)
        elif exponent < 0:
            base = ComplexNumber(self.real, self.imag)
            exponent = -exponent
            base = base.conj() / base.norm()
        else:
            base = ComplexNumber(self.real, self.imag)

        result = ComplexNumber(1, 0)
        while exponent > 0:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2

        return result

    # 複素数の文字列表現
    def __str__(self):
        if self.imag == 1:
            return f"{self.real} + i"
        elif self.imag == -1:
            return f"{self.real} - i"
        elif self.imag > 0:
            return f"{self.real} + {self.imag}i"
        elif self.imag == 0:
            return f"{self.real}"
        else:
            return f"{self.real} - {-self.imag}i"
