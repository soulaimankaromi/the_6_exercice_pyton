nom1=int(input("Type the first number"))
nom2=int(input("Type the second number"))
f=0
d=0
for i in range (2,nom1) :
    if nom1%i==0 :
        d=d+i
for i in range (2,nom2) :
    if nom2%i==0 :
        f=f+i
if d==nom2 and f==nom1 :
    print("The two numbers are friends")
else :
    print("The two numbers are not friends")