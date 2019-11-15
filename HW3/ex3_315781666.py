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
    # count longest repetition of c in string s
    max_rep = 0
    for length in range(len(s)+1):
        search_string = length*c
        if search_string in s:
            max_rep = length

    return max_rep
    pass  # replace this with your implementation


#########################################
# Question 4 - do not delete this comment
#########################################
def upper_strings(lst):
    if type(lst) != type(list()):
        return -1
    working_list = []
    for thing in lst:
        if type(thing) == type(str()):
            working_list.append(thing.upper())
        else:
            working_list.append(thing)

    lst = working_list
    return lst
    # replace this with your implementation


#########################################
# Question 5 - do not delete this comment
#########################################
def div_mat_by_scalar(mat, alpha):
    new_matrix = [[], []]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            new_matrix[i].append(mat[i][j]//alpha)

    return new_matrix
    # replace this with your implementation


#########################################
# Question 6 - do not delete this comment
#########################################
def mat_transpose(mat):
    # Create a list of all numbers...
    numbers_in_mat = []
    for row in mat:
        for number in row:
            numbers_in_mat.append(number)

    # build matrix placeholder
    new_matrix_cols = len(mat)
    new_matrix_rows = len(mat[0])
    new_matrix = [[0]*new_matrix_rows]*new_matrix_cols

    # fill matrix
    for a in range(new_matrix_rows):
        new_matrix[a] = numbers_in_mat[0+a :: new_matrix_cols]

    return new_matrix
    # replace this with your implementation
