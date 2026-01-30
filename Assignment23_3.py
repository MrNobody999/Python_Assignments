class Numbers:
    def __init__(self, value):
        self.Value = value

    def SumFactors(self):
        factor_sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                factor_sum += i
        return factor_sum

    def ChkPerfect(self):

        return self.SumFactors() == self.Value

    def ChkPrime(self):

        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print(f"Factors of {self.Value}: ", end="")
        factors_list = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors_list.append(i)
        print(factors_list)


num1 = Numbers(6)
print(f"Number: {num1.Value}")
print(f"Is prime? {num1.ChkPrime()}")
print(f"Is perfect? {num1.ChkPerfect()}")
num1.Factors()
print(f"Sum of factors : {num1.SumFactors()}")

num2 = Numbers(13)
print(f"Number: {num2.Value}")
print(f"Is prime? {num2.ChkPrime()}")
print(f"Is perfect? {num2.ChkPerfect()}")
num2.Factors()
print(f"Sum of factors : {num2.SumFactors()}")

num3 = Numbers(12)
print(f"Number: {num3.Value}")
print(f"Is prime? {num3.ChkPrime()}")
print(f"Is perfect? {num3.ChkPerfect()}")
num3.Factors()
print(f"Sum of factors : {num3.SumFactors()}")

num4 = Numbers(28)
print(f"Number: {num4.Value}")
print(f"Is prime? {num4.ChkPrime()}")
print(f"Is perfect? {num4.ChkPerfect()}")
num4.Factors()
print(f"Sum of factors : {num4.SumFactors()}")
