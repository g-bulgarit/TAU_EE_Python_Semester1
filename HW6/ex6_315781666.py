''' Exercise #6. Python for Engineers.'''

#########################################
# Question 1.a - do not delete this comment
#########################################
def four_bonacci_rec(n):
    if n <= 3:
        return n
    else:
        return (four_bonacci_rec(n-1) +
                four_bonacci_rec(n-2) +
                four_bonacci_rec(n-3) +
                four_bonacci_rec(n-4))

#########################################
# Question 1.b - do not delete this comment
#########################################
def four_bonacci_mem(n, memo=None):
    # Same as last question, but save results in
    # dictionary before returning them...

    if n <= 3:
        return n
    if memo == None:
        memo = {}
    if n not in memo:
        memo[n] = (four_bonacci_mem(n - 1, memo) +
                   four_bonacci_mem(n - 2, memo) +
                   four_bonacci_mem(n - 3, memo) +
                   four_bonacci_mem(n - 4, memo))
    return memo[n]

#########################################
# Question 2 - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    # Same idea as last time...
    if n == 1:
        return 1
    if n == 2:
        return 2
    if memo == None:
        memo = {}
    if n not in memo:
        memo[n] = (climb_combinations_memo(n-1, memo) +
                   climb_combinations_memo(n-2, memo))
    return memo[n]


#########################################
# Question 3 - do not delete this comment
#########################################
def catalan_rec(n,memo=None):
    if memo == None:
        # Fabricate dictionary for memoization
        memo = {}
        memo[0] = 1
        memo[1] = 1

    if n in memo:
        # If already encountered - return the value instead of computing
        return memo[n]

    else:
        next_cat_value = 0
        for index in range(n):
            next_cat_value += catalan_rec(index, memo) * catalan_rec(n-1-index, memo)
            memo[n] = next_cat_value
        return next_cat_value



#########################################
# Question 4.a - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    if n == 0:
        return 1
    elif n < 0 or not lst:
        return 0

    return find_num_changes_rec(n-lst[0], lst) + \
           find_num_changes_rec(n, lst [1:])

#########################################
# Question 4.b - do not delete this comment
#########################################
def find_num_changes_mem(n, lst, memo=None):
    if n == 0:
        return 1
    if not memo:
        memo = {}
    elif n < 0 or not lst:
        return 0
    # key = [tuple((n, tuple(lst))),
    #         tuple((n - lst[0], tuple(lst))),
    #         tuple((n, tuple(lst[1:])))]
    key = tuple((n, tuple(lst[1:])))
    if key not in memo:
        memo[tuple((n - lst[0], tuple(lst)))] = find_num_changes_mem(n - lst[0], lst, memo)
        memo[tuple((n, tuple(lst[1:])))] = find_num_changes_mem(n, lst[1:], memo)

    return memo[tuple((n - lst[0], tuple(lst)))] + memo[tuple((n, tuple(lst[1:])))]



#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

#Question 1.a tests - you can and should add more    
# print(four_bonacci_rec(0) == 0)
# print(four_bonacci_rec(5) == 12)
# print(four_bonacci_rec(8) == 85)
#
# #Question 1.b tests - you can and should add more
# print(four_bonacci_mem(0) == 0)
# print(four_bonacci_mem(5) == 12)
# print(four_bonacci_mem(8) == 85)
# print(four_bonacci_mem(100) == 14138518272689255365704383960)
# #Question 2 tests - you can and should add more
# print(climb_combinations_memo(4) == 5)
# print(climb_combinations_memo(42) == 433494437)

#Question 3 tests - you can and should add more    
# cat_list = [1,1,2,5,14,42,132,429]
# print(catalan_rec(3))
# for n,res in enumerate(cat_list):
#     print(catalan_rec(n) == res)
# #
# # #Question 4.a tests - you can and should add more
# print(find_num_changes_rec(5,[1,2,5,6]) == 4)
# print(find_num_changes_rec(4,[1,2,5,6]) == 3)
# print(find_num_changes_rec(4,[1,2,5,6]))
# print(find_num_changes_rec(0.9,[1,2,5,6]) == 0)
# print(find_num_changes_rec(1,[2,5,6]) == 0)
# print(find_num_changes_rec(-1,[1,2,5,6]) == 0)
# print(find_num_changes_rec(2,[0.5,1]) == 3)


# Question 4.b tests - you can and should add more
print(find_num_changes_mem(5,[1,2,5,6]) == 4)
print(find_num_changes_mem(4,[1,2,5,6]) == 3)
print(find_num_changes_mem(960,[1,2,5,6,13]))
# print(find_num_changes_mem(0.9,[1,2,5,6]) == 0)

# ============================== END OF FILE =================================