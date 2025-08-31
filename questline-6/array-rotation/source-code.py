#CODE:
n=int(input("Enter the number of elements:"))
nums=list(map(int,input("Enter the elements:").split()))
print("The list before rotation:",nums)
k=int(input("Enter k:"))
newlst=nums.copy()
for i in range(k):
    for j in range(len(nums)):
        newlst[j]=nums[j-1]
    nums=newlst.copy()
print("The list after rotation:",nums)
