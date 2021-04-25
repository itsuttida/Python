#ผลรวมของตัวเลข
#เช่น รับ input เป็นจำนวนรอบ
#ถ้าจำนวนรอบคือ 3 = 1 + 2 +3   , 5 = 1+2+3+4+5


count = int(input("ใส่จำนวนรอบ : "))  #รับจำนวนรอบ

sum = 0
for i in range(1,count+1) :
    sum = sum + i


print("sum : ", sum)




