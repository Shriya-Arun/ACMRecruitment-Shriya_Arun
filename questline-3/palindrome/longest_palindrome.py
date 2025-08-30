#CODE:
def palindrome(string):
    words=string.lower().split()
    palindrome=""
    for i in words:
        if i[::-1]==i:
            if len(i)>len(palindrome):
                palindrome=i
    print("The longest palindrome is:",palindrome)  
string=input("Enter the string:")
palindrome(string)

'''OUTPUT:
Enter the string: Anna checked the radar at noon
The longest palindrome is: radar'''
