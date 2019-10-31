''' Exercise #1 - Python.'''

#########################################
# Question 1 - do not delete this comment
#########################################
R = 5 # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 1 below here.

pi = 3.14 # we define pi like this...
circle_diameter = 2*R
circle_circumference = 2*pi*R
circle_area = pi*(R**2)

# Print the required stuff...
print("Diameter is: " +str(circle_diameter))
print("Circumference is: " +str(circle_circumference))
print("Area is: " +str(circle_area))

#########################################
# Question 2 - do not delete this comment
#########################################
S = "Hello" # Replace ??? a string of your choice.
# Write the rest of the code for question 2 below here.

if len(S) > 10:
    S_1 = S[0:10].lower()
    S_2 = S[10:].upper()
    print(S_1 + S_2)
else:
    print("$" + S[1:-1] + "@")

#########################################
# Question 3 - do not delete this comment
#########################################
number  = 542 # Replace ??? with a int of your choice.
# Write the rest of the code for question 3 below here.

if number % 2 == 0:
    # Number is even...
    print("I am " + str(number) + " and I am even")
else:
    print("I am " + str(number) + " and I am odd")

#########################################
# Question 4 - do not delete this comment
#########################################
a = 9 # Replace ??? with a positive int of your choice.
b = 5  # Replace ??? with a positive int of your choice.
c = 5  # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 4 below here.

first_calc = (a + b) ** (1 / c)
second_calc = (a ** b) ** (1 / c)
third_calc = (a / b) - (b / c)

print("{:.5f}".format(first_calc))
print("{:.5f}".format(second_calc))
print("{:.5f}".format(third_calc))

#########################################
# Question 5 - do not delete this comment
#########################################
year = 2004 # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 5 below here.

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")


