from person import Person

class Student(Person):
    def __init__(self, name,age,profession):
        super().__init__(name, age)
        self._profession=profession

    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, value):
        self._profession = value

    @profession.deleter
    def profession(self):
        del self._profession

    def say_my_profession(self):
        return f"{super().preset_me()} and i'm {self.profession}"
