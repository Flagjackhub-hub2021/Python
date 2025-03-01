"""
Catatan Penting !!!

Dalam Penerapan Operator Logika (Logika), itu bisa di terabkan di semua 
Tipe Data Casting di Python (Implict, Explicit, Inference)
"""

print("=====Ini adalah Casting Inference pada Python menggunakan Logika : And , OR ===== ")

Variable_and         = True
Variable_diskonjuksi = False | (Variable_and)

print(Variable_diskonjuksi)
print("\n")


print("=====Ini adalah Casting Inference pada Python menggunakan Logika : OR , And ===== ")

Variable_diskonjuksi = False | True 
Variable_and         = False and (Variable_diskonjuksi)

print(Variable_and)
print("\n")


print("=====Ini adalah Casting Inference pada Python menggunakan Logika : OR , Not ===== ")

Variable_diskonjuksi = False | True 
Variable_not         = not True and  (Variable_not)

print(Variable_not)
print("\n")


print("=====Ini adalah Casting Inference pada Python menggunakan Logika : Not , And ===== ")

Variable_not = not False and True
Variable_and = True and (Variable_not)

print(Variable_and)
print("\n")


print("=====Ini adalah Casting Inference pada Python menggunakan Logika : Not , OR ===== ")

Variable_not = not True and False
Variable_or  = False | (Variable_not)

print(Variable_or)
print("\n")


print("=====Ini adalah Casting Inference pada Python menggunakan Logika : OR , X-OR ===== ")

Variable_or  = True
Variabel_XOR = True ^ (Variable_or)

print(Variabel_XOR)
print("\n")


print("=====Ini adalah Casting Inference pada Python menggunakan Logika : IF , THEN ===== ")

Variable_IF   = True
Variable_THEN = True and (Variable_IF)

print (Variable_THEN)
print("\n")


print("=====Ini adalah Casting Inference pada Python menggunakan Logika : THEN , IF ===== ")

Variable_THEN   = False
Variable_IF     = True and (Variable_THEN)

print (Variable_IF)
print("\n")


print("=====Ini adalah Casting Inference pada Python menggunakan Logika : IF , And Only IF ===== ")

Variable_IF          = True
Variable_And_Only_IF = True and (Variable_IF)

print (Variable_And_Only_IF)
print ("\n")


"""
Ini adalah impelementasi dari Inference Casting 
dalam memnggunakan Gerbang Logika (Operator Logika).
Akan tetapi, hanya menggunakan 1 Nilai table di dalamnya 
"""
