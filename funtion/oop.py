class Staff:
    def __init__(self, name, age, job):
        self.name=name
        self.age=age
        self.job=job
    def people(self):
        return f'{self.name} is {self.age} years old, and is a {self.job}'

f1=Staff('angela', 30, 'teacher')
print(f1.people())
