first = input("First name: ").strip()
last = input("Last name: ").strip()
full = first.capitalize() + " " + last.capitalize()
age = int(input("Age: "))

print(f"HEllo {full}, next year you will be {age + 1}.")
