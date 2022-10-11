arr=[5,8,4,6,9,2]
n=len(arr)
if n==0:
    print("searching not possible")

target=10
if target not in arr:
    print("not there")
for data in range(0,n):
    if target==arr[data]:
        print("target is at index :  {0} ".format(data))
    else:
        pass


