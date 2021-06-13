
#รับค่าเข้าไปใน list จนกว่าจะใส่เลขที่ น้อยกว่า 0 และเรียงลำดับตัวเลข

number = []
while True:
    x = int(input("ป้อนตัวเลขของคุณ : "))
    if x < 0 :
        break
    number.append(x)

print("ก่อนเรียง : ", number)
number.sort()  #น้อยไปมาก
print("น้อยไปมาก : ", number)
number.reverse()  #มากไปน้อยฃ
print("มากไปน้อย : ", number)


