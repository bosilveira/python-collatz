from collatz import Collatz

if __name__ == '__main__':
    for x in range(1,24):
        c = Collatz(x)
        print(c.eq_numeric())
        print(c.eq_factored())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
