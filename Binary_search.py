def search(arr,target,start,end):
    n=len(arr)
    if(n==0):
        print("operation not possible")
    start=0
    end=n
    while start<=end:
        mid=(start+end)//2
        if(target==arr[mid]):
            return mid
        elif target<arr[mid]:
            end=mid-1
        else:
            start=mid+1



arr=[1,2,3,4,5,6,7,8]
target=7
start = 0
end = len(arr)
result=search(arr,target,start,end)
print("element is at index: {0} ".format(result))