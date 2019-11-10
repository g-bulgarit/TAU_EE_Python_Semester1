""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 3  # Replace the assignment with a positive integer to test your code.
A = [1, 2, 3, 4, 5]  # Replace the assignment with other lists to test your code.

divisible_idx = -1
for number in A:
    if number % a == 0:
        # Set divisible_idx as the index of num.
        divisible_idx = A.index(number)
print(divisible_idx)


# Write the code for question 2 using a for loop below here.

# Write the code for question 2 using a while loop below here.


# End of code for question 1

#########################################
# Question 2 - do not delete this comment
#########################################
B = ['hello', 'world', 'course', 'python', 'day']
# Replace the assignment with other lists of strings (str) to test your code.


# Write the rest of the code for question 2 below here.

# For loop variant:
letter_sum = 0
for in_str in B:
    letter_sum += len(in_str)

avg_str_len = letter_sum/len(B)
stdev_counter = 0

for in_str in B:
    if len(in_str) > avg_str_len:
        stdev_counter += 1

print("The number of strings longer than the average is: " +str(stdev_counter))

# While loop variant:
idx = 0
letter_sum_w = 0
while idx < len(B):
    # Iter over all strings in B
    letter_sum_w += len(B[idx])
    idx += 1

avg_str_len_w = letter_sum_w/len(B)
stdev_counter_w = 0

idx =0
while idx < len(B):
    if len(B[idx]) > avg_str_len_w:
        stdev_counter_w += 1
    idx += 1

print("The number of strings longer than the average is: " +str(stdev_counter_w))

# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

C = [0, 1, 2, 3, 4]  # Replace the assignment with other lists to test your code.


# Write the rest of the code for question 3 below here.
if len(C) == 0:
    print("0")
elif len(C) == 1:
    print(str(C[0]))
else:
    placeholder = 0
    for idx in range(0,len(C)-1):
        placeholder += (C[idx] * C[idx+1])
    print(placeholder)



# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

D = [1, 2, 4, 6, 5, 9]    # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 4 below here.
final_list = []
abs_val_list = [0]
final_list.append(D[0])

for index in range(0, len(D)-1):
    abs_dis = abs(D[index+1] - D[index])

    if abs_dis > max(abs_val_list):
        final_list.append(D[index+1])

    if abs_dis not in abs_val_list:
        abs_val_list.append(abs_dis)




print(final_list)


# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'abaadddefggg'  # Replace the assignment with other strings to test your code.
k = 3  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.
subst =""
attempted_chars = []
done_flag= False
for char in my_string:
    if char in attempted_chars:
        pass
    else:
        attempted_chars.append(char)
        pattern = str(k*char)
        if pattern in my_string:
            print("For length " + str(k) + ", found the substring " + str(pattern) + "!")
            done_flag = True
            break

if done_flag == False:
    print("Didn't find a substring of length " + str(k))
# End of code for question 5