# Example of magic methods.

class Fraction:
    def __init__(self, num, den):
        gcd = Fraction.gcd(num, den)
        self.num = num / gcd
        self.den = den / gcd
    
    def __str__(self):
        return f'{self.num}/{self.den}'

    # Sum two fractions.
    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        new_frac = Fraction(new_num, new_den) 

        return new_frac
    
    @staticmethod
    def gcd(a, b):
        while(a, b) > 0:
            a, b = b, a % b

if __name__ == '__main__':
    frac_1 = Fraction(0, 0)
    frac_2 = Fraction(0, 0)
    sum_frac = frac_1 + frac_2

    print(f'Suma = {sum_frac}')