#Plaindrome
s = input("Enter a string to check for palindrome:  ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        print("Palindrome")
    else:
        print("Not a Palindrome")
ans = isPalindrome("dad")