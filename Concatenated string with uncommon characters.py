s1='aacdb'
s2='gafd'
a=set(s1)
b=set(s2)
s1=list(a.symmetric_difference(b))
o=''
for i in s1:
    o=o.__add__(i)

print(o)

