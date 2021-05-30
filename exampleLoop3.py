
#สร้างขอบตาราง

"""
input = 4

จะแสดง
XXXX
X  X
X  X
XXXX
"""

"""
input = 6

จะแสดง
XXXXXX
X    X
X    X
X    X
X    X
XXXXXX
"""

last = int(input(" ป้อน = "))

for row in range (1, last+1):   #row =2
    for conlumn in range(1, last+1 ):  #column = 1
        if row == 1 or row == last or conlumn == last or conlumn == 1:
            print( "X" , end='')
        else:
            print(" " , end='')
    print ("")