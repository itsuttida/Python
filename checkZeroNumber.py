
# เขียนโปรแกรมรับ input 1 ตัว เป็นจำนวนเต็ม
# ตรวจสอบว่ามีค่ามากกว่า 0 หรือไม่
# ถ้ามากกว่า ให้พิมพ์ more than zero
# ถ้าน้อยกว่าหรือเท่ากับ ให้พิมพ์ less or equal than zero

num = int(input())

if num > 0 :
    print("more than zero")
elif num <= 0:
    print("less or equal than zero")
# else :
#     print("less or equal than zero")
# if num <= 0 :
#     print("less or equal than zero")