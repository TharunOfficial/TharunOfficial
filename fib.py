list1=[]
a=input("enter at least two mumber")
for i in a:
     list1.append(int(i))
for i in range(100):
    add=list1[-1]+list1[-2]
    list1.append(add)
    print(list1)
 
