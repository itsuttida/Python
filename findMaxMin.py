#ใส่ตัวเลขเรื่อยๆ แล้วหาว่าตัวไหนมากที่สุด น้อยที่สุด จะจบเมื่อใส่เลข 0

max = 0
min = 9999999999999
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

        

        #list  score = [1,2,3,4,5,6,7,7]
        #dict  {
            "nick" : 10,
            "aew" : 12,
        # }