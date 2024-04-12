class Collatz:
    """
    A class to generate and manipulate Collatz sequences with modified rules.

    In this context, the Collatz equation takes the form
    ((3**log3) * m + n) / (2**log2)
    where m represents the initial number, and n denotes a series that emerges during the cycle calculation.

    Author:
        Braulio Silveira <bosilveira@gmail.com>

    Attributes:
        m (int): The initial number for the Collatz sequence.
        log2 (int): The exponent of 2 in the modified Collatz sequence.
        log3 (int): The exponent of 3 in the modified Collatz sequence.
        n (list): List of exponents of 3 in the modified Collatz sequence.
        cycle (list): The modified Collatz sequence.
    """
    def __init__(self, m=1, log2=0, log3=0, n=None, cycle=None):
        """
        Initializes a Collatz object.

        Args:
            m (int): The initial number for the Collatz sequence. Default is 1.
            log2 (int): The exponent of 2 in the modified Collatz sequence. Default is 0.
            log3 (int): The exponent of 3 in the modified Collatz sequence. Default is 0.
            n (list): List of exponents of 3 in the modified Collatz sequence. Default is None.
            cycle (list): The modified Collatz sequence. Default is None.

        Note:
            If `n` and `cycle` are not provided, the `calculate()` method is called to generate them.
        """
        self.m = m
        self.log2 = log2
        self.log3 = log3
        self.n = [] if n is None else n
        self.cycle = [] if cycle is None else cycle
        if n is None or cycle is None:
            self.calculate()

    def __str__(self):
        """
        The string representation of the modified Collatz sequence.

        Returns:
            str: A string representation of the modified Collatz sequence.
        """
        result = f"{self.cycle}"
        return result

    def eq_factored(self):
        """
        The equation representing the modified Collatz sequence in factored form.

        Returns:
            str: The equation representing the modified Collatz sequence in factored form.
        """
        result = "[" if self.log3 > 0 else '('
        result += f"3^{self.log3} * x"
        result += f" + ({' + '.join(self.series_n())})]" if self.log3 > 0 else ')'
        result += f" / 2^{self.log2} - 1 = 0"
        return result

    def eq_numeric(self):
        """
        The equation representing the modified Collatz sequence in numeric form.

        Returns:
            str: The equation representing the modified Collatz sequence in numeric form.
        """
        result =  "(" if self.log3 > 0 else ''
        result += f"{3**self.log3} * x" if self.log3 > 0 else 'x'
        result += f" + {self.numeric_n()})" if self.log3 > 0 else ')'
        result += f" / {2**self.log2}" if self.log2 > 0 else ''
        result += ' - 1 = 0'
        return result

    def series_n(self):
        """
        Generates the series representing the exponents of 3 in the modified Collatz sequence.

        Returns:
            list: List of strings representing the series of exponents of 3.
        """
        result = []
        for i in range(len(self.n)):
            result.append(f"3^{(len(self.n) - 1 - i)} * 2^{self.n[i]}")
        return result

    def numeric_n(self):
        result = 2**self.log2 - (self.m * (3**self.log3))
        return result

    def calculate(self):
        self.log2 = 0
        self.log3 = 0
        self.n = []
        self.cycle = [self.m]
        base = self.m
        while base != 1:
            if base % 2 == 0:
                base = base // 2
                self.cycle.append(base)
                self.log2 += 1
            else:
                base = (3 * base + 1) // 2
                self.cycle.append(base)
                self.n.append(self.log2)
                self.log2 += 1
                self.log3 += 1
        return self
