f1=open('mydata','r')
print(f1.readline(),end="")
print(f1.readline(),end="")
print(f1.readline(4))

f2=open('def','w')
for data in f1:
    f2.write(data)
