class User:
    def __init__(self,name="",age=None):
        self._name=name
        self._age=age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name=value
    @name.deleter
    def name(self):
        del self._name

    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age=value
    @age.deleter
    def age(self):
        del self._age
    
    def __str__(self):
        return f"""Hi my name is: {self._name} and i have {self._age} years old"""

def main():
    user1=User("simon",16)
    print(user1)

if __name__=="__main__":
    main()