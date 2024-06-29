class Dog:

    def __init__(self,kind):
        self.kinds = ["bull","husky","knine"]

    def __repr__(self) -> str:

        return f"Dog name is {self.name} and kind is {self.kind}"

    def f():
        """TODO: Docstring for f.

        :arg1: TODO
        :returns: TODO

        """
        return "hello"

    @classmethod
    def get(cls):
        """TODO: Docstring for g.

        :arg1: TODO
        :returns: TODO

        """
        name = input("Name: ")
        kind = input("Kind: ")

        return cls(name,kind)
#------------------------------------------------------------------------


def main():
    """TODO: Docstring for main.

    :arg1: TODO
    :returns: TODO

    """
    dog = Dog.get()
    print(dog)


if __name__ == "__main__":
    main()
