import random as rm

class Hat:
    def __init__(self) -> None:
        self.houses = ["Itarsi","Ahmedabad","Maninagar"]

    def sort(self,name):
        print(name,"is in",rm.choice(self.houses))



hat = Hat()
hat.sort("pratham")
