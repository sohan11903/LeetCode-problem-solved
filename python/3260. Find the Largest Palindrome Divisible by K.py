n = 1
k = 4
a="0"
x=[]
i=1
while(len(a)<=n):
    a=str(i*k)
    if a[:n-2] == a[-(n-2):]:
        x.append(a)
    i+=1
print(x[len(x)-1])