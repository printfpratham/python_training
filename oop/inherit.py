class Wizard:
    def __init__(self,name):
        """TODO: Docstring for __init__.

        :arg1: TODO
        :returns: TODO

        """
        if not name:
            raise ValueError("No name")
        self.name = name
        print(self.name)
    ...

class Student(Wizard):
    def __init__(self,name,house):
        """TODO: Docstring for __init__.

        :arg1: TODO
        :returns: TODO

        """
        super().__init__(name)
        self.house = house
        print(self.house)
    ...

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
        print(self.subject)
    ...


name = input("Enter name: ")
house = input("Enter house: ")
subject = input("Enter Subject: ")
wizard = Wizard(name)
student = Student(name,house)
professor = Professor(name,subject)









