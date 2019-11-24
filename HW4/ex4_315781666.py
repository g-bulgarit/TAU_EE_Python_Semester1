''' Exercise #4. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def second_most_popular_character(my_string):
    letter_dict = {}

    for char in my_string:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1

    max = sorted(list(letter_dict.values()))[-2]

    candidates = []
    for thing in letter_dict:
        if letter_dict[thing] == max:
            candidates.append(ord(thing))

    return chr(min(candidates))

print(second_most_popular_character("HelloWorld"))
print(second_most_popular_character("cccaabb"))
#########################################
# Question 2 - do not delete this comment
#########################################
def diff_sparse_matrices(lst):

    pass  # remove this


#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_locations(s, k):
    
    pass  # remove this

#########################################
# Question 4 - do not delete this comment
#########################################
def count_lines(in_file, out_file):
    pass #replace this with your implementation

#########################################
# Question 5 - do not delete this comment
#########################################
def simple_sent_analysis(in_file):
    pass #replace this with your implementation


#########################################
# Question 6 - do not delete this comment
#########################################
def calc_profit_per_group(in_file):
    pass #replace this with your implementation

#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

# ============================== END OF FILE =================================
