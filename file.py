print(3)
#1 1 50 = 3710
#2 2 30 = 7350

hr = int (input(" จำนวนชั่วโมง "))
minute = int (input(" จำนวนนาที "))
sec = int (input(" จำนวนวินาที "))

number = (hr * 3600) + (minute * 60) + (sec)  #หาวินาทีรวม
print(number)