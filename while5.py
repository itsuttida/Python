#รับตัวเลขไปเรื่อยๆ จนกว่าผลบวกจะมากกว่า 100

sum = 0
while sum <= 100 :
    number = int(input("ป้อนตัวเลขของคุณ : "))
    # sum = sum+number
    sum += number
    print("sum : " , sum)