# Belajar list
thislist = ["pisang", "Anggur", "Apple"]
print(thislist)
print("\n")

# pembanding + operator
a = 33
b = 200
if b > a:
    print("b lebih besar dari a ?")
print("\n")

# melakukan penginputan angka menggunkan while
f = 1
while f < 6:
    print(f)
    f += 1
print("\n")


# Melakukan break pada list
buah = ["pisang", "Anggur", "Apple"]
for x in buah:
    print(x)



# Melakukan panggilan Hello World dalam function
print("\n")
def function():
    print("Hello World form function")

function()
print("\n")


# Membuat perkalian tampa melakakun deklarasi variable
x = lambda a, b : a * b
print(x(5, 6))
print ("\n")


# Membuat biodata 

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age  = age

p1 = Person("Muhammad Fadel", 20)
p2 = Person("Muhammad Fadel", 23)

print(p1.name)
print(p1.age)



