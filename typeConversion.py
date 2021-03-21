#Type Conversion

x = 10  #int
y = 3.1
z = "20"

print(type(x))
print(type(y))
print(type(z))

result = x + int(z) #str -> int
print("result = ", result)


result2 = str(x) + z   #integer -> string
print("result2 = ", result2)

result3 = y + float(z)  #string -> float
print("result3 = ", result3)

result4 = str(y) + z #float -> string
print("result4 = ", result4)

print(float(x))  #int -> float

print(int(y))  #float -> int


a = "aew"
print(int(a))