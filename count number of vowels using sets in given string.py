a='Hello World'
b=[]
count=0
for i in a:
    b.append(i)
c=['a','e','i','o','u']
print(b)
for i in range(0,len(b)):
    if b[i] in c:
        count=count+1
print("No. of vowels :",count)