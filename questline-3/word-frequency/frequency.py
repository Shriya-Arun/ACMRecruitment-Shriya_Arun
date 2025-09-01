#code
fr=open("Demofile.txt","r")
data=fr.read().lower().split()
d={}
for i in data:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for key,value in sorted(d.items(),key= lambda item:item[1],reverse=True):
    print(key,value,sep="--->")
    
