def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 4, 5, 6, 7, 8))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(3, add=4, multiply=5)

