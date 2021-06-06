#การเข้าถึงข้อมูลใน list

number = [1,2,3,4,5,6]   #สมาชิิกคือ 1-6
name = ["นาย A","นาย B","นาย C"]
all = [10 , "นาย A ", True , 3.14 , -10]


print(number[3])

print(number[1]+number[2])

print(name[1])

#ระบุค่าติดลบ

print(number[-1])
print(name[-2])

#ระบุเป็นช่วง

print(all[1:3])
print(all[-3:-1])
print(all[-3:])
print(all[:3])
print(all[1:])