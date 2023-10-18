tab1=[]
t=[]
s=0
n=int(input("Type the number of students :"))
for i in range (0,n) :
    a=int(input("Type the note "))
    while a<0 or a>20 :
       a=int(input("Type in note a number between 0 and 20 "))
    tab1.append(a)
    s=s+a
e=s/n
for i in range (0,n) :
    if tab1[i]>e :
        t.append(tab1[i])
print("Grades above averge are :",t)