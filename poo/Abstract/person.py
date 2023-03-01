class Person:
    def __init__(self,name,age) -> None:
        self._name=name
        self._age=int(age)

    #name methods
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name=value
    @name.deleter
    def name(self):
        del self._name

    #age methods
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age=value
    @age.deleter
    def age(self):
        del self._age
    
    def preset_me(self):
        return f"Hi my name is {self.name}, i have {self.age} years old"
