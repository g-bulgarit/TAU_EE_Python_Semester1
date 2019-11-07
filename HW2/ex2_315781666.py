""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 3  # Replace the assignment with a positive integer to test your code.
A = [1, 2, 3, 4, 5]  # Replace the assignment with other lists to test your code.

divisible_idx = None
for idx, number in enumerate(A):
    if number % a == 0:
        # Set divisible_idx as the index of num.
        divisible_idx = idx
        break

if divisible_idx is None:
    print("-1")
else:
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



# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

C = [0, 1, 2, 3, 4]  # Replace the assignment with other lists to test your code.


# Write the rest of the code for question 3 below here.



# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

D = [1, 2, 4, 7]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 4 below here.



# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'abaadddefggg'  # Replace the assignment with other strings to test your code.
k = 3  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.



# End of code for question 5