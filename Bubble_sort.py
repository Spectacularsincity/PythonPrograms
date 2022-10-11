def sort(arr,n):
    if(n==0 or n==1):
        print("sorting not possible")
    else:
        for i in range(0,n-1):
            for j in range(0,n-(i+1)):
                if arr[j]>arr[j+1]:
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp
    print(arr)


arr=[5,4,3,2,1]
n=len(arr)
print("elements before sorting: ")
print(arr)
print("elements after sorting : ")
sort(arr,n)
