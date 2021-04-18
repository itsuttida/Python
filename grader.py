
#เกรด  0,1,2,3,4
#ข้อมูลนำเข้า คือ คะแนนสอบ
#ประมวลผลว่าอยู่ในเกรดไหน
#พิมพ์ว่าได้เกรดไหน

score = int(input("Input your score : "))

if score >= 0 and score <= 100:
    if score >= 80:
        print("เกรด 4")
    elif score >= 70 :
        print("เกรด 3")
    elif score >= 60 :
        print("เกรด 2")
    elif score >= 50 :
        print("เกรด 1")
    else :
        print("เกรด 0")

else :
    print("ใส่เลขผิด")
    