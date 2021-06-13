
#รับค่าเข้าไปใน list จนกว่าจะใส่เลขที่ น้อยกว่า 0 และหาเลขมากสุด น้อยสุด ผมรวม

number = []
while True:
    x = int(input("ป้อนตัวเลขของคุณ : "))
    if x < 0 :
        break
    number.append(x)

print("number : ", number)
print("ค่าน้อยสุด = " , min(number))
print("ค่ามากสุด = " , max(number))
print("หาค่าผลรวม = " , sum(number))
