p=[]
n=int(input("Type the number :"))
for i in range (1,n) :
    s=0
    for j in range (1,i+1) :
        if i%j==0 :
            s=s+1
    if s==2 :
      p.append(i)
print("Prime integers less than",n,"are :",p)