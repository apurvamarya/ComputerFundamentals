# A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(A[2:5])
# #Hello, World!
# #0123456789
# B = "0123456789"
# print(B[7:9])
# print(len(B))
# c = "Hello, World!"
# u = C.upper()
# print(u)
# d = 'HE went to Rohan\'s house'
# print(d)
# c.stripe()
# c.lstrip()
# c.rstrip()
# c.capitalize()
# for i in range(1,6):
#     print(f"Hello {i}")
# old = "hello world"
# old = old.replace("world","python")
# print(old) 
# firstName= "Apurvam"
# lastName= "Arya"
# age = 19
# print(f"Hello, my name is {firstName} {lastName} and I am {age} years old") 
# print("Hello, my name is {} {} and I am {} years old" .format(firstName, lastName, age)) 
# a = "My, name, is, Apurvam"
# print(a.split(","))
# print(a.find("Apurvam"))
# print(a.count("is"))
# print(a.isalnum())
# print(a.isalpha())
# A= ["Apple", "Orange", "Papaya"]
# for i in A:
#     print(i)
# for i in range(0,3):
#     print(A[i])
text = "Hello, World!"
count = 0
for char in text:
    if char.lower() in "aeiou":
        count+= 1
print(count)