#รับคะแนนของนักศึกษากลุ่มหนึงแล้วทำการแสดงผล จะหยุดรับเมื่อมีการป้อน -1 

score = int(input("คะแนนสอบ : "))

while score != -1:
    print(score)
    score = input("คะแนนสอบ : ")
    score = int(score)
