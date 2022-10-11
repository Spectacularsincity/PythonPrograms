f=open("mydata","r")
#print(f.read())
print(f.readline(),end="")
print(f.readline(),end="")
print(f.readline(4))

#f1=open('abc','w')
#f1.write("something")
#f1.write('people')

f1=open('abc','a')
f1.write('mobile')


for data in f:
    f1.write(data)
