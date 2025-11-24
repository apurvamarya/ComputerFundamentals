from dataclasses import dataclass

@dataclass
class student:
    name : str
    age : int
    grade : float
student1 = student("Apurvam", 20, 85.5)
print(student1)