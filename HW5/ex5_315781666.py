''' Exercise #5. Python for Engineers.'''
#########################################
# Question 1 - do not delete this comment
#########################################
def reverse_string(s):
    # If we have a string of length 1, it is it's own inverse.
    if len(s) == 1:
        return s
    else:
        # Otherwise, return the last character and keep going
        # in the same fashion until only one character remains.
        return s[-1]+reverse_string(s[:-1])

#########################################
# Question 2 - do not delete this comment
#########################################
def find_maximum(lst):
    # Exactly following the provided instructions...
    # If we get an empty list - return -1
    if len(lst) == 0:
        return -1
    # If we get only one element, it
    # has to be the maximum...
    if len(lst) == 1:
        return lst[0]
    # Otherwise, check if the last element of the list
    # Is the largest.
    else:
        if lst[-1]> find_maximum(lst[0:-1]):
            return lst[-1]
        else:
            return find_maximum(lst[0:-1])

#########################################
# Question 3 - do not delete this comment
#########################################
def is_palindrome(s):
    # If we managed to go over the entire string without returning false,
    # return true.
    if len(s) == 1 or len(s) == 0:
        return True

    # Check if the first and last characters are the same,
    # if they are, call the function again with -1 symmetric offset from both sides.
    if s[0] == s[-1] and is_palindrome(s[1:-1]):
        return True
    else:
        return False

#########################################
# Question 4 - do not delete this comment
#########################################
def climb_combinations(n):
    # Basically fibonacci...
    # to climb n steps, we have
    if n == 1:
        return 1  # one option to climb one step
    if n==2:
        return 2 # two options to climb two steps
    else:
        return climb_combinations(n-1) + climb_combinations(n-2)

#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_paren(s, cnt=0):
    lookout = ["(", ")"]  # characters that I should not remove

    # Check length of string, if it is zero - we check cnt
    if len(s) == 0:
        if cnt != 0:
            return False
        else:
            return True

    # If the string is not of length zero yet,
    # check if the first character is parenthesis, if not - remove it.
    if s[0] not in lookout:
        s = s[1:]

    # Check what kind of parenthesis are we looking at,
    # add or subtract one to check symmetry.
    if s[0] == "(":
        cnt += 1
    elif s[0] == ")":
        cnt -= 1

    # Call the function again without the first character
    # until all characters run out.
    return is_valid_paren(s[1:], cnt)



#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################

print(reverse_string("abc") == 'cba')
print(reverse_string("Hello!") == '!olleH')

print(find_maximum([9,3,0,10]) == 10)
print(find_maximum([9,3,0]) == 9)
print(find_maximum([]) == -1)

print(is_palindrome("aa") == True)
print(is_palindrome("aa ") == False)
print(is_palindrome("caca") == False)
print(is_palindrome("abcbbcba") == True)

print(climb_combinations(3) == 3)
print(climb_combinations(10) == 89)

print(is_valid_paren("(.(a)") == False)
print(is_valid_paren("p(()r((0)))") == True)
print(is_valid_paren("p((()r((0)))") == False)
print(is_valid_paren("p(((r((0)))))") == True)

# ============================== END OF FILE =================================
