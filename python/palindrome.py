def check_if_palindrome(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] -= 1
        else:
            count_dict[c] = 1

    count = 0
    for k in count_dict:
        if count_dict[k] >= 1:
            count+=1
    
    if count > 1:
        return False
    else:
        return True

def check_palindrome(string):
    rev = string[::-1]
    if rev == string:
        print(f"{string} is a palindrome")
    elif check_if_palindrome(string):
        print(f"{string} can become a palindrome")
    else:
        print(f"{string} cannot become a palindrome")
        
check_palindrome('RACECRA')