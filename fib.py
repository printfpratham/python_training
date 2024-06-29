def fib(n):
    """TODO: Docstring for function.

    :arg1: TODO
    :returns: TODO

    """
    result = []
    a , b = 0 , 1
    while a < n:
        a , b = b,a+b
        result.append(a)
    return result

x = int(input("Enter X:"))

f = fib(x)
print(f)
a = tuple(f)
print(a)

