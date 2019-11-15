''' Exercise #3. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def sum_divisible_by_k(lst, k):
    sum_ph = 0
    is_div_by_k = 0
    for number in lst:
        if number % k == 0:
            sum_ph += number
            is_div_by_k = 1

    if is_div_by_k:
        return sum_ph
    else:
        return 0
    # replace this with your implementation


#########################################
# Question 2 - do not delete this comment
#########################################
def mult_odd_digits(n):
    mult_ph = 1
    for char in str(n):
        if int(char) % 2 != 0:
            mult_ph *= int(char)

    return mult_ph
    # replace this with your implementation


#########################################
# Question 3 - do not delete this comment
#########################################
def count_longest_repetition(s, c):
    pass  # replace this with your implementation


#########################################
# Question 4 - do not delete this comment
#########################################
def upper_strings(lst):
    pass  # replace this with your implementation


#########################################
# Question 5 - do not delete this comment
#########################################
def div_mat_by_scalar(mat, alpha):
    pass  # replace this with your implementation


#########################################
# Question 6 - do not delete this comment
#########################################
def mat_transpose(mat):
    pass  # replace this with your implementation



#-----------
test_f1_lst = [45.5, 60, 73, 48]
f1_k = 4
print(sum_divisible_by_k(test_f1_lst, f1_k))


print(mult_odd_digits(2048))