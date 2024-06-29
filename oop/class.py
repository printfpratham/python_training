class Dog:

    def __init__(self,name,kind):
        self.name = name
        self.kind = kind
    def __repr__(self) -> str:

        return f"Dog name is {self.name} and kind is {self.kind}"

    def f():
        """TODO: Docstring for f.

        :arg1: TODO
        :returns: TODO

        """
        return "hello"
#getter functions
    @property
    def name(self):
        """TODO: Getter function for Name

        :arg1: TODO
        :returns: self._name

        """
        return self._name

    @name.setter
    def name(self,name):
        if name not in ["bunny","sunny","tommy"]:
            raise ValueError("No such name")
        self._name = name

    @property
    def kind(self):
        return self._kind

#setter function
    @kind.setter
    def kind(self,kind):
        if kind not in ["K9","bull","labra"]:
            raise ValueError("Not a breed")
        self._kind = kind


#------------------------------------------------------------------------


def main():
    """TODO: Docstring for main.

    :arg1: TODO
    :returns: TODO

    """
    dog = get_dog()
    print(dog)

def get_dog():
    """TODO: Docstring for g.

    :arg1: TODO
    :returns: TODO

    """
    name = input("Dog name: ")
    kind = input("kind: ")
    x  = Dog.f()
    print(x)
    return Dog(name,kind)


if __name__ == "__main__":
    main()
