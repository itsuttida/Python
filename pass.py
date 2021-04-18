
#pass คือให้ผ่านไปก่อน ยังไม่ต้องทำอะไร

score = int(input("Input your score : "))

if score >= 0 and score <= 100:
    if score >= 80:
        pass
    elif score >= 70 :
        print("เกรด 3")
    elif score >= 60 :
        print("เกรด 2")
    elif score >= 50 :
        pass
    else :
        print("เกรด 0")

else :
    print("ใส่เลขผิด")