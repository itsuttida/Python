#ทายผลลูกเต๋า ถ้าถูก แสดง ได้รับรางวัล ถ้าผิด แสดง เสียใจด้วย
#สุ่มไปเรื่อยๆ จนกว่าจะใส่เลขที่น้อยกว่า 0 หรือ 
#ให้สุ่มแค่ 3 ครั้ง  หรือ 
#หรือทายถูก ก็ออก

import random

myrandom = random.randrange(1,7)   
count = 0

while True :
    number = int(input("ทายตัวเลข : "))

    if number < 0 or number == 3 :
        break
    correct = (number == myrandom)
    if not correct:
        if number > myrandom:
            print("น้อยกว่า")
        if number < myrandom:
            print("มากกว่า")
    if correct :
        print("ได้รับรางวัล")
        break
    else :
        print("เสียใจด้วย")
    count += 1
    