dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
for i in dic1:
    dic4[i]=dic1[i]
for j in dic2:
    dic4[j]=dic2[j]
    if 40 in dic2:
        dic4[2]=dic4[2]+dic2[2]
for k in dic3:
    dic4[k]=dic3[k]
print(dic4)
    

# {1: 10, 2: 60, 3: 30,  5: 50, 6: 60} 