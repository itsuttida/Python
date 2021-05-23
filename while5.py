#รับตัวเลขไปเรื่อยๆ จนกว่าผลบวกจะมากกว่า 100

sum = 0
while sum < 100 :
    number = input("ป้อนตัวเลขของคุณ : ")
    # sum = sum+number
    sum += int(number)
    print("sum : " , sum)