def sort(nums):
        for i in range(5):
            minpos=i
            for j in range(i,6):
                if(nums[j]<nums[minpos]):
                    minpos=j


            temp=nums[i]
            nums[i]=nums[minpos]
            nums[minpos]=temp

            #print(nums)
        print(nums)

arr=[5,3,8,6,7,2]
print("elements before sorting: ")
print(arr)
print("elements after sorting : ")
sort(arr)