class records:
    def __init__ (self, name, age, roll):
        self.name=name
        self.age=age
        self.roll=roll
    def display(self):
        print(self.name)
        print(self.age)
        print(self.roll)
record=records("a","17","1")
record.display()
        