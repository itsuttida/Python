#คำนวณค่า BMI

#BMI = น้ำหนัก (Kg) / ส่วนสูง * ส่วนสูง (m)

# input / 

weight = int(input("น้ำหนักของคุณ (kg) : "))
high = int(input("ส่วนสูงของคุณ (cm) : "))

#process
# high = high / 100
high /= 100

bmi = weight / high ** 2

#output

print("BMI = " , int(bmi))
