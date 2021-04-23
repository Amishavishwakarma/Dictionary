word="MISSISSIPPI"
dic={}
count=0
for i in word:
    print(i)
    if i not in dic:
        count=count+1
        dic[i]=count
print(dic)   