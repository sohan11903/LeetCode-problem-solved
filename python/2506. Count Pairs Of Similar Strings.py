words = ["aba","aabb","abcd","bac","aabc"]
d=set(words[0])
c=1
o=[]
for i in range(1,len(words)):
    print(d,set(words[i]))
    if d == (set(words[i])):
        c+=1
        print(c)
    else:
        o.append(c)
        d=set(words[i])
        c=1
o.append(c)        
        
print(max(o))
    