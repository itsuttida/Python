#สร้างภาพวาด 4 เหลี่ยมจตุรัส
# 

"""
input = 2

จะแสดง
XX
XX
"""


"""
input = 3

จะแสดง
XXX
XXX
XXX
"""

"""
input = 4

จะแสดง
XXXX
XXXX
XXXX
XXXX
"""


last = int(input(" ป้อน ="))

for row in range (1, last+1):
    for conlumn in range(1, last+1 ):
        print( "X" , end='')
    print ("")