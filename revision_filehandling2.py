f1=open('img.jpg','rb')
f2=open('def.jpg','wb')

for data in f1:
    f2.write(data)
    