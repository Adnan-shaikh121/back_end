def is_palindrome(s):
    # Remove spaces and punctuation
    s = ''.join(e for e in s if e.isalnum())
    
    # Convert to lowercase
    s = s.lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Take input from user
input_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
