#ผลรวมของตัวเลข
#เช่น รับ input เป็นจำนวนรอบ
#ถ้าจำนวนรอบคือ 3 = 1 + 2 +3   , 5 = 1+2+3+4+5

count = int(input("ใส่จำนวนรอบ : "))

sum = 0

i = 1  #ตัวนับรอบ

while i <= count:
    print("รอบที่ : ",i , "จะได้ " ,sum , " + ",i)
    sum = sum + i
    print("ค่า Sum = ", sum)
    i = i+1
