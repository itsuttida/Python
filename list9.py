#การรวมข้อมูล

number = [1,2,3,4,5,5,5,5,5,5]   #สมาชิิกคือ 1-6

fruit = ["มะม่วง","มะนาว","มะยม","มะละกอ","มะกอก"]

all = number + fruit

print("all = ", all)

#มีเลข 5 อยู่กี่ตัว

count = all.count(5)
print("count = ", count)

#รวมสมาชิกโดยใช้ list เดิม

number.extend(fruit)
print("number = ", number)


