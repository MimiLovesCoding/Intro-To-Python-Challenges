# Homework Lesson 10 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

################################################################################
### When solving coding challenges, think about the time complexity (Big O). ###
################################################################################

# Challenge 1
# Multiplication of a three-digit number
#
# A program gets a three-digit number and has to multiply all its digits.
# For example, if a number is 349, the code has to print the number 108, because 3*4*9 = 108.
#
# Hints:
# Use the modulus operator % to get the last digit.
# Use floor division to remove the last digit
def multiply_digits(number):
    # Your code here

    if number < 100 or number > 999:
        raise ValueError("The number must be a three-digit number.")

    last_digit = number % 10
    number = number // 10
    middle_digit = number % 10
    first_digit = number // 10

    result = first_digit * middle_digit * last_digit

    return result


three_digit_number = 253
result = multiply_digits(three_digit_number)
print(f"The product of the digits of {three_digit_number} is {result}")


# ---------------------------------------------------------------------

# Challenge 2
# Sum and multiplication of even and odd numbers.
#
# You are given an array of integers. Your task is to calculate two values: the sum of
# all even numbers and the product of all odd numbers in the array. Please return these
# two values as a list [sum_even, multiplication_odd].
#
# Example
# For the array [1, 2, 3, 4]:
#
# The sum of all even numbers is 2 + 4 = 6.
# The product of all odd numbers is 1 * 3 = 3.
# The function should return the list [6, 3].

def sum_even_and_product_odd(arr):
    # Initialize variables for the sum of even numbers and the product of odd numbers
    sum_even = 0
    product_odd = 1
    odd_exists = False
    # Your code here

    for num in arr:
        if num % 2 == 0:
            sum_even += num
        else:
            product_odd *= num
            odd_exists = True


if not odd_exists:
    product_odd = 0  # if there are no odd numbers, set product to 0

return [sum_even, product_odd]

array = [1, 2, 3, 4, 5, 6]
result = calculate_sum_and_product(array)
print(f"The sum of even numbers and the product of odd numbers is: {result}")

# ---------------------------------------------------------------------

# Challenge 3
# Invert a list of numbers
#
# Given a list of numbers, return the inverse of each. Each positive becomes a negative,
# and the negatives become positives.
#
# Example:
# Input: [1, 5, -2, 4]
# Output: [-1, -5, 2, -4]

def invert_numbers(numbers):
# Your code here
return [-num for num in numbers]

numbers_list = [1, -2, 3, -4, 5]
inverted_list = invert_numbers(numbers_list)
print(f"The inverted list is: {inverted_list}")


# ---------------------------------------------------------------------

# Challenge 4
# Difference between
#
# Implement a function that returns the difference between the largest and the
# smallest value in a given list.
# The list contains positive and negative numbers. All elements are unique.
#
# Example:
# Input: [3, 5, 7, 2]
# Output: 7 - 2 = 5

def max_diff(arr):
    # Check if the list is empty
    # If it is, return 0 as there's no difference to be calculated
    if len(arr) == 0:
        return 0

# If the list is not empty,
# proceed with the rest of the code.

# Your code here


# ---------------------------------------------------------------------

# Challenge 5
# Sum between range values
# You are given an array of integers and two integer values, min and max.
# Your task is to write a function that finds the sum of all elements in the
# array that fall within the range [min, max], inclusive.
#
# Example:
# arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
# min_val = 3
# max_val = 7
#
# Output: 25 (3 + 4 + 5 + 6 + 7)
#
# Hint:  Iterate through each number (num) in the array (arr) and check if the current number  falls within the range [min_val, max_val].

#def sum_between_range(arr, min_val, max_val):
# Your code here
