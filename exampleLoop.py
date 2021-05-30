#ตัวเลขขั้นบันได

""" 
input = 6

1
12
123
1234
12345
123456

"""

last = int(input("ป้อนตัวเลข = "))  #last = 6

for row in range(1,last+1):   #row = 6
    for conlumn in range(1,row):  #conlumn = 5
        print(conlumn , end='')
    print("")

"""
เว้นบรรทัด
1
12
123
1234

"""