T1=[]
T2=[]
T=[]
n=int(input("Type size n of both tables"))
for i in range (0,n) :
    t1=int(input("Type the number for table 1"))
    T1.append(t1)
for i in range (0,n) :
    t2=int(input("Type the number for table 2"))
    T2.append(t2)
for i in range (0,n) :
    s=T1[i]+T2[i]
    T.append(s)
print("The sum of tables T1 and T2",T)