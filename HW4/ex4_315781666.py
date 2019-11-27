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
    # create a new matrix(dict) that is empty.
    output_mat = {}

    # add all values of each matrix in matrix list,
    # if value already exists - subtract,
    # otherwise - add new value to the output matrix.

    for matrix in lst:
        for key_tuple in matrix:
            try:
                # If the value exist- this operation is valid
                output_mat[key_tuple] -= matrix[key_tuple]
                if output_mat[key_tuple] == 0:  # if 0 is left, delete it.
                    output_mat.pop(key_tuple)
            except KeyError:
                # if the value does not exist - add it.
                output_mat[key_tuple] = matrix.get(key_tuple)

    return output_mat  # remove this


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

#########################################
# Question 4 - do not delete this comment
#########################################
def count_lines(in_file, out_file):

    with open(in_file, 'r') as fp:
        lines = len(fp.readlines())
        fp.close()

    with open(out_file, 'w') as wf:
        wf.write(str(lines))
        wf.close()

#########################################
# Question 5 - do not delete this comment
#########################################
def simple_sent_analysis(in_file):
    forbidden_chars = ["!", "?", "-", ";", "$", "%",".", ","]
    output_dict = {"happy":0, "sad":0}
    try:
        with open(in_file, 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                line = line.strip().lower().split(" ")  # Sanitize a bit...

                for word in line:
                    # Sanitize moreeeeeeeee
                    if word[0] in forbidden_chars:
                        word = word[1:]
                    if word[-1] in forbidden_chars:
                        word = word[:-1]

                    # Check sentiment
                    if word == "happy":
                        output_dict["happy"] += 1
                    if word == "sad":
                        output_dict["sad"] += 1
            fp.close()
            return output_dict
    except IOError:
        print("Cannot encode " + str(in_file) + " due to IO error")
        return output_dict

#########################################
# Question 6 - do not delete this comment
#########################################
def calc_profit_per_group(in_file):
    allowed = ["happy", "sad", "neutral"]
    output_dict = {"happy" : 0,
                   "sad" : 0,
                   "neutral" : 0}
    try:
        lines = []
        with open(in_file, 'r')as fp:
            for line in fp.readlines():
                lines.append(line)
            fp.close()

        #     Work on the acquired lines...
        #     Perform Checks:
        seen_series = []
        for line in lines:
            line = line.strip().split(",")
            if len(line) != 3:
                raise ValueError("Invalid input")

            try:  # Test if it's a number
                q = float(line[1]) /2
            except ValueError:
                 raise ValueError("Invalid input")

            if str(line[2]).strip() not in allowed:
                raise ValueError("Invalid input")

            series_name = str(line[0]).strip()
            if series_name not in seen_series:
                seen_series.append(series_name)
            else:
                raise ValueError("The series " + series_name + " appears more than once")

        #   Now continue
        happy_counter = 0
        neutral_counter = 0
        sad_counter = 0

        for series in lines:
            # Sanitize lines:


            series = series.strip().split(",")
            series_profit = float(series[1])
            series_profile = str(series[2]).strip()
            output_dict[series_profile] += series_profit
            if series_profile == "happy": happy_counter+=1
            if series_profile == "sad": sad_counter+=1
            if series_profile == "neutral": neutral_counter+=1


        #   Replaces 0s in the dict with NA
        for key in output_dict:
            if output_dict[key] == 0:
                output_dict[key] = "NA"
            else:
                if key == "happy": output_dict[key] /= happy_counter
                if key == "sad": output_dict[key] /= sad_counter
                if key == "neutral": output_dict[key] /= neutral_counter


    except IOError:
        print("Cannot use " + str(in_file) + " due to IO error")
    return output_dict

print(calc_profit_per_group("q6_input_good_example_1.csv"))
#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

# ============================== END OF FILE =================================
