#ใส่ตัวเลขเรื่อยๆ แล้วหาว่าตัวไหนมากที่สุด น้อยที่สุด จะจบเมื่อใส่เลขน้อยกว่า 0

max = 0
min = 9999999999999999
# max , min = 0,0

while True :
    number = int(input("ป้อนตัวเลขของคุณ : "))
    if number < 0:  #ออกจาก loop 
        break
    if number > max:   
        max = number  
    if number < min:
        min = number

print("max : ", max)
print("min : ", min)

    