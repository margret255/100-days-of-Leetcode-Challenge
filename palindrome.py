def palindrome(y):
    #negative numbers cant be palindromes
    if y <0:
        return False
    #convert the number to a string and reverse it

    original=str(y)
    reversed_number=original[::-1] #using slicing

    return original == reversed_number
#test function
print(palindrome(343))
print(palindrome(-343))
print(palindrome(340))
print(palindrome(0))
