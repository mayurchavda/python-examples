input = "Was it a car or a cat I saw".lower()
input = ''.join(ch for ch in input if ch.isalnum())
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

if(is_palindrome(input)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")