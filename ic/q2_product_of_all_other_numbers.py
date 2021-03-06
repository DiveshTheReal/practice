# You have a list of integers, and for each index you want to find the 
# product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() 
# that takes a list of integers and returns a list of the products.

# Example:
#   [1, 7, 3, 4] - - - > [84, 12, 28, 21]

# Approach 1: Brute force Approach [O(n^2)]
# def get_products_of_all_ints_except_at_index(list):
#   new_list = []
#   for index1, val in enumerate(list):
#     result = 1
#     for index2, val in enumerate(list):
#       if index1 == index2:
#         continue
#       result *= list[index2]
#     new_list.append(result)
#   return new_list


# Approach 2
def get_products_of_all_ints_except_at_index(int_list):

    # make sure we have at least 2 numbers
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other indices requires at least 2 numbers')

    # we make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    i = 0
    while i < len(int_list):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

    # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    i = len(int_list) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]
        i -= 1

    return products_of_all_ints_except_at_index

list = [1, 7, 3, 4]

print get_products_of_all_ints_except_at_index(list)