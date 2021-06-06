#การเพิ่มข้อมูลเข้าไปใน list

number = [1,2,3,4,5,6]   #สมาชิิกคือ 1-6

fruit = ["มะม่วง","มะนาว","มะยม"]

print("ก่อนเพิ่ม == > ", fruit)

#append() นำสมาชิกใหม่ ไปต่อท้ายเพื่อน

fruit.append("มะปราง")
fruit.append("แตงโม")
print("หลังเพิ่ม == > ", fruit)

#insert (index , สมาชิกใหม่) การแทรก
fruit.insert(1,"ทุเรียน")
print("หลังแทรก == > ", fruit)
