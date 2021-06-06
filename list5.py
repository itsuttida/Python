number = [1,2,3,4,5,6]   #สมาชิิกคือ 1-6

fruit = ["มะม่วง","มะนาว","มะยม"]

#เช็คว่าเป็นสมาชิกใน list นี้หรือเปล่า
if 20 in number:
    print("เป็น")
else:
    print("ไม่เป็น")


#จำนวนสมาชิก

# print(len(fruit))

#นำขนาดของ list ไปทำงานกับ loop for

for i in range(len(fruit)):
    print(fruit[i])