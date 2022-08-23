f1=open("dad.txt")
m=f1.readlines()
i=0
c=0
while i<len(m):
    c=c+1
    i+=1
print(c)
f1.close()