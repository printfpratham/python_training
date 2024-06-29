import random

class Company:

    employee = ["Pratham","Tarang","Mehul","Hiren"]


    @classmethod
    def sort(cls,name):
        """TODO: Docstring for s.
        :arg1: TODO
        :returns: TODO
        """
        print(random.choice(cls.employee),"is working in",name)
        return cls.employee



#emp = Company()
Company.sort("Silicon Signals")
#print(x)

