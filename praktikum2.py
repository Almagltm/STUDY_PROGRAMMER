#python file : praktikum 2 PTI
# outhor     : Alma Murael Gultom

#1. Variable Deklaration

#2. operations-> +,-,*,/,%,=

#3. Perulangan -> Looping
#for statement
#index data-> dimulai 0
for baris in range(5):
    for kolom in range(4):
         print("*",end="")
    print()

print('================')

#while iteration -> need ccondition

baris2 = 0
tengah = 5
while baris2 < 5:
    kolom2 = 0
    if(baris2 % 2 == 1):
        while kolom2 < 5:
            if(kolom2 == int(round(tengah/2))):
                print("*",end="")
            else:
                print(" ",end="")
            kolom2 += 1
    else:
        while kolom2 < 5:
            print("*",end="")
            kolom2 += 1
    print() 
    baris2 += 1     

      
