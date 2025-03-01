# Operator Logika Not, dan Tipe data Bool
x = 5
not x < 10
False
not callable(x)
True

x = 5, not x < 10, not callable(x)
print(x)

print("\n", 10 * "=", "\n")


# Operator Logika Or, dan Tipe data Bool
x = 5
x < 10 or callable(x)
True
x < 0 or callable(x)
False

x = 5, x < 10 or callable(x), x < 0 or callable(x)
print(x)

print("\n", 10 * "=", "\n")


# Operator Logika And, dan Tipe data Bool
x = 5
x < 10 and callable(x)
False
x < 10 and callable(len)
True

x = 5, x < 10 and callable(x), x < 10 and callable(len)
print(x)

