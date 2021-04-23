list1=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
] 
b=[]
for i in list1:
    for j in i:
        a=i[j]
        if a not in b:
            b.append(a)
print(b)
        
