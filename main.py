# # Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a, b, c):

    return max(a, b, c)

# Example 
number1 = 10
number2 = 20
number3 = 15

maximum = max_num(number1, number2, number3)
print("The maximum number is:", maximum)

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for number in numbers:
        result *= number

    return result
#Example
my_list=[2,4,6,8]
result = mult_list(my_list)
print(result)    

# Write a Python function called rev_string() to reverse a string.
def rev_string(strg):
    return strg[::-1]
#Example
print(rev_string("pineapple"))

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(x,a,b):
    return x in range(a,b+1)

# Example
print(num_within(7,6,8))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    def generate_next_row(prev_row):
        row = [1]
        for i in range(len(prev_row) - 1):
            row.append(prev_row[i] + prev_row[i + 1])
        row.append(1)
        return row

    if n <= 0:
        return

    current_row = [1]
    for _ in range(n):
        print(current_row)
        current_row = generate_next_row(current_row)

# Example usage:
n = 3
pascal(n)
