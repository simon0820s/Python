class Figure:
    def __init__(self):
        self._name=""
        self._sides=None
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def sides(self):
        return self._sides
    
    @sides.setter
    def sides(self, value):
        self._sides = value

    def __str__(self):
        return str({"name":self.name,"sides":self.sides})
        
def run():
    square=Figure()
    sides=int(input("please enter the sides of your figure => "))
    name=input("please enter the name of your figure => ")
    square.sides=sides
    square.name=name

    print(square)


if __name__=='__main__':
    run()
