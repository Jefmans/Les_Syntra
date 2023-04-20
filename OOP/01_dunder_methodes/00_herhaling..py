

class Person:
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = self._define_fullname()

    
    def __str__(self):
        return  f"{self.first_name} - {self.last_name} - {self.age}"
    
    def _define_fullname(self):
        return self.first_name + " " + self.last_name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

        

class Student(Person):
    
    def __init__(self, first_name, last_name, age, jaar):
        super().__init__(first_name, last_name, age)
        self.jaar = jaar

