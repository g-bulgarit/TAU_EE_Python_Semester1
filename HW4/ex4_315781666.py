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

#########################################
# Question 2 - do not delete this comment
#########################################
def diff_sparse_matrices(lst):

    pass  # remove this


#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_locations(s, k):
    # for every two characters, make a dictionary entry
    output_dict = {}
    for char_loc in range(0, len(s)-k+1):
        chars = s[char_loc:char_loc+k]

        if chars not in output_dict:
            output_dict[chars] = []

        for position in range(len(s)-k+1):
            pair = s[position:position+k]
            if pair == chars:
                if position not in output_dict[chars]:
                    output_dict[chars].append(position)

    return output_dict

print(find_substring_locations("Hello World", 3))
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
