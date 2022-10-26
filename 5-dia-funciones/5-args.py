def suma_pedagogo(*args):
    total=0
    for item in args:
        total+=item
    return total
print(suma_pedagogo(5,9,8,89,5,6,2,10))


def suma(*args):
    return sum(args)
print(suma(5,9,8,89,5,6,2,0))