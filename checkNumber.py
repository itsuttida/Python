#รับตัวเลข 1 ตัว
#เช็คว่าเป็น เลขคู่หรือคี่

#2  = 2 is even
#5  = 5 is odd

number = int (input( " enter number " ))
if number % 2 == 0 :
    print( " %d is even " %(number))

else : 
    print( " %d is odd" %(number))