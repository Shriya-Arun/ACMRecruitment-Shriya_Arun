#iterative
s=input("Enter the string:")
s2=""
for i in range(len(s)-1,-1,-1):
    s2+=s[i]
print("Iterative method:",s2)

#recursive
def reversal_str(string):
    if len(string)==0:
        return string
    else:
        return(reversal_str(string[1:])+string[0])
string=input("Enter the string:")
print("Recursive method:",reversal_str(string))
