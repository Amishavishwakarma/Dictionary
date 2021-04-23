dic ={
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
a=[]
b=[]
for i in dic:
    i=dic[i]
    a.append(i)
print(a)
i=0
mix=a[0]
while i<len(a):
    if a[i]>mix:
        mix=a[i]
    i=i+1
b.append(mix)
a.remove(mix)
j=0
mix=a[0]
while j<len(a):
    if a[j]>mix:
        mix=a[j]
    j=j+1
b.append(mix)
a.remove(mix)
k=0
mix=a[0]
while k<len(a):
    if a[k]>mix:
        mix=a[k]
    k=k+1
a.remove(mix)
b.append(mix)
print(b)




