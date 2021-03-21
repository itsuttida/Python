#โปรแกรมเช็คเลขคู่เลขคี่
#รับตัวเลข 1 ตัว
#เช็คว่าเป็น เลขคู่หรือคี่

#2  = 2 is even
#5  = 5 is odd

number = int (input( " enter number " ))
if number % 2 == 0 :  #ใช้ mod (%) การหารเอาเศษ เพราะเลขคู่ถ้าหารด้วย 2 จะได้เศษ 0
    print( " %d is even " %(number))   #print ได้ 3 วิธี
    print(" " + str(number) + " is even " )
    print(" ",number," is even " ,2,2,2,"aew")

elif number % 2 != 0 :
    print( " %d is odd" %(number))

#หรือใช้ else
# else : 
#     print( " %d is odd" %(number))
