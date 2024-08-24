import math
eq = "1+x+2+3+x+x=x+8+4+3" 
i=0
x1=0
num1=0
x2=0
num2=0
neg=None
while i < len(eq):
    while eq[i]!="=":
        if eq[i]=="-": neg=True
        elif eq[i] == "+": neg = False
        if eq[i]=="x":
            x1+=1
            i+=1
        elif eq[i]=="+" or eq[i]=="-":
            i+=1
        else:
            if neg==False:
                num1+=int(eq[i])
                print(num1)
            else:
                num1-=int(eq[i])
                print(num1)
            i+=1
    i=i+1
    while i < len(eq):
        if eq[i]=="-": neg=True
        elif eq[i] == "+": neg = False
        if eq[i]=="x":
            x2+=1
            i+=1
        elif eq[i]=="+" or eq[i]=="-":
            i+=1
        else:
            if neg==False:
                num2+=int(eq[i])
            else:
                num2-=int(eq[i])
            i+=1
v1=x1-x2
v2=num2-num1
if v2==0:
    print("x=0")
else:
    s=math.gcd(v1,v2)
    print("x="+str(int(v2/s)))