# Dict Clear
fadel = {"Name": "Muhammad Fadel", "Age": 20}
fadel.clear()
print(fadel)
print("\n")

"""
Mengapus data pada elemen variable fadel dalam Array
"""

# Dict Copy
a = {"Name": "Muhammad Fadel", "age": 20}
b = a.copy()
b ["age" ] = 30
c = a.copy()
c ["age" ] = 40
print(a)

print(b)
print(c)
print("\n")

"""
Melakukan pengcopyan terhadap data di variable a ke b dalam 
elemen Array
"""

# Dict get
d = {"Name": "Muhammad Fadel", "Age": 20, "Year": 2003}
age = d.get("Age")
print(age)

Name = d.get("Name")
print(Name)

Year = d.get("Year")
print(Year)
print("\n")

"""
Melakukan deklarasi pengambilan data terhadap variable d, di dalam elemen 
Array, dan membuat variable baru dengan nama elemen, yang berada di dalam 
elemen Array
"""
# d = {"Name": "Muhammad Fadel", "Age": 20}
# age = d.get("Age")
# print(age)

# occupation = d.get("ocupation")
# print(occupation)

# occupation = d.get
# ("occupation", "unemployed")

# print(occupation)


# Dict items
e = {"Name": "Muhammad Fadel", "Age": 20, "Year": 2003}
items = e.items()
print(items)
print("\n")

"""
Hanya menggambil semua elemen Array di variable e
"""

# Dict Key
f = {"Name": "Muhammad Fadel", "Age": 20, "Year": 2003}
keys = f.keys()
print(keys)
print("\n")

"""
Hanya menggambil elemen (Name,Age,Year) Array di varibale f
"""

# Dict values
g = {"Name": "Muhammad Fadel", "Age": 20, "Years": 2003}
values = g.values()
print(values)
print("\n")

# dict pop 
h = {"Name": "Muhammad Fadel", "Age": 20, "Year": 2003}
Age = h.pop("Age")
print(Age)
print(h)
print("\n")

# Dict update
i = {"Name": "Muhammad Fadel", "Age": 20, "Year": 2003, "County": "Indonesia"}
i.update({"age":30})
print(i)

# Dict setdefault
j = {"Name": "Muhammad Fadel", "Age": 20, "Year": 2003}
country = j.setdefault("Country","Indonesia")
print(country)
print(j)