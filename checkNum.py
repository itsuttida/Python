#เขียนโปรแกรมรับ input 1 ตัว เป็นจำนวนเต็ม
# ตรวจสอบว่ามากกว่า 0 ให้พิมพ์  num > 0
# ตรวจสอบว่าน้อยกว่า 0 ให้พิมพ์  num < 0
# ตรวจสอบว่าเท่ากับ 0 ให้พิมพ์  num = 0

num = int(input())

if num > 0 :
    print (num , " > 0")

elif num < 0 :
    print ( num , " < 0 ")

elif num == 0 :
    print ( num , " = 0 ")

