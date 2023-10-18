tab=[]
n=int(input("Type the number :"))
s=0
for i in range (1,n+1) :
    if n%i==0 :
        s=s+1
        tab.append(i)
print("The number of divisors are: ",s)
print("The divisors of a number are :",tab)
