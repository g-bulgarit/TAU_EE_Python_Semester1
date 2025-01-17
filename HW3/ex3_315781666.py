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
    out_matrix = []
    for i in range(len(mat)):
        line = []
        for j in range(len(mat[i])):
            line.append(mat[i][j]//alpha)
        out_matrix.append(line)

    return out_matrix
    # replace this with your implementation


#########################################
# Question 6 - do not delete this comment
#########################################
def mat_transpose(mat):
    output_mat = []

    for column in range(len(mat[0])): # For every column of the input matrix,
        line = []  # Create a new empty list, to which we will add all mat[row][column] values
        for row in range(len(mat)):
            line.append(mat[row][column])  # Add these values to the line
        output_mat.append(line)  # Add the as a row to our 'final matrix' - now we have 1 row, let's continue...
    return output_mat
