# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# For example:

# sum_to(6)  # returns 21
# sum_to(10) # returns 55

def sum_to(n):
    if n == 0:
        return n
    else:
        prev_n = sum_to(n-1)
        result = prev_n + n
        return result

print(sum_to(6), "<< adds all numbers 6, 5, 4, 3, 2, 1")
print(sum_to(10), "<< adds all numbers up to 10")


# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

# For example:

# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest(*args):
    for arg in args:
        biggest = max(arg)
    return biggest

print(largest([1, 28, 3, 9, 0]), "<< largest number from list[1, 28, 3, 9, 0]")
print(largest([10, 4, 2, 231, 91, 54]), "<< largest from list[10, 4, 2, 231, 91, 54]")

# Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurances(str1, str2):
    count = 0
    while str2 in str1:
        count += 1
        str1 = str1[str1.find(str2) + 1:]
    return count

# For example:

print(occurances('fleep floop', 'e'))   # returns 2
print(occurances('fleep floop', 'p'))   # returns 2
print(occurances('fleep floop', 'ee'))  # returns 1
print(occurances('fleep floop', 'fe'))  # returns 0



# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).

def product(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

# For example:

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0