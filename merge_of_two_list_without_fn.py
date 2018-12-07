list1 = [25, 18, 9, 41, 26, 31]
list2 = [25, 45, 3, 32, 15, 20]
m=len(list2)
for i in range(0,m):
    list1.append(list2[i])
l=len(list1)
arr=list1
for i in range(l):
    for j in range(0,l-i-1):
        if (arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("output",arr)