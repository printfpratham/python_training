def pyramind(n):
    """TODO: Docstring for pyramind.

    :arg1: TODO
    :returns: TODO

    """
    for i in range(1,n+1):
        for j in range(n-i):
            print("\n",end="")

        for k in range(1,2*i):
            print("1",end="")

x = int(input("Enter num"))
pyramind(x)

