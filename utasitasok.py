'''
ismeteld=True
while ismeteld:
    ismeteld:False
    kezdo=int(input("Kérem a kezdő számot: "))
    veg=int(input("Kérem a veg számot: "))
    lepes=int(input("Kérem a lepesközt: "))


    if kezdo < veg and lepes > 0 :
        while kezdo <= veg:
            print(kezdo)
            kezdo += lepes

    elif kezdo > veg and lepes < 0 :
        while kezdo >= veg:
            print(kezdo)
            kezdo += lepes
    else:
        print("hibás adatok")
        ismeteld=True
'''
#----------
kezdo=1
veg=12
lepes=2

for i in range(kezdo,veg,lepes):
    print(i)


kezdo=1
veg=12
lepes=-2

for i in range(kezdo,veg,lepes):
    print(i)


kezdo=12
veg=2
lepes=-2

for i in range(kezdo,veg,lepes):
    print(i)


kezdo=12
veg=2
lepes=0
#for i in range(kezdo,veg,lepes):
#    print(i)
