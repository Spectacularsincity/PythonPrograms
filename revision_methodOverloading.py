class A:
    def Add(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            return a+b+c
        elif (a!=None and b!=None):
            return a+b
        else:
            return a
a=A()
print(a.Add(34,56,78))
print(a.Add(45,67))
print(a.Add(99))


