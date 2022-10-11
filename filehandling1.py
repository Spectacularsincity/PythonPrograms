f1=open('img.jpg','rb')

f=open('abc.jpg','wb')

for data in f1:
    f.write(data)
