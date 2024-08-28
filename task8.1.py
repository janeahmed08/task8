lst=[]
n=int(input("enter num of elements"))
sorted=True

for o in range(n):
    elmnts=int(input())
    lst.append(elmnts)
print(lst)

for i in range(len(lst)-1) :
#for j in range(i+1,len(lst)-1):
    if lst[i]<=lst[i+1]:
        sorted=True
        continue
    elif lst[i]>lst[i+1]:
        sorted=False
        print(False) 
if sorted==True:
    print(True)