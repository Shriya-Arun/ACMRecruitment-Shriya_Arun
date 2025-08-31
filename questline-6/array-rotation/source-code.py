n=int(input("enter the number of elements:"))
nums=list(map(int,input("Enter the elements:").split()))
k=int(input("Enter k:"))
newlst=nums.copy()
for i in range(k):
    for j in range(len(nums)):
        newlst[j]=nums[j-1]
    nums=newlst.copy()
print(nums)
