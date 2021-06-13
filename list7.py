#การลบข้อมูลออกจาก list

number = [1,2,3,4,5,6,7,8,9,10]   #สมาชิิกคือ 1-6

fruit = ["มะม่วง","มะนาว","มะยม","มะละกอ","มะกอก"]
print(" ก่อน ====> ", fruit)

fruit.remove("มะยม")

print("หลัง remove ====> ", fruit)

fruit.pop()    #ลบตัวท้ายสุดออก
print("หลัง pop ====> ", fruit)


del fruit[0]   #ลบด้วย index
print("หลัง del ====> ", fruit)


#ลบสมาชิกทั้งหมดออกจาก list

fruit.clear()
print("หลัง clear ====> ", fruit)


