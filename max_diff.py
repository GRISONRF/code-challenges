# Given a list of N integers, output the maximum difference of two elements where the large
# number appears after the smaller number.

# Input
# The first line of the input consists of an integer - inputArr size, representing the size of the list(N)
# The second line of the input consists of Nspace-separated integers - inputAr representing
# the elements of the given list.

# Output
# Print an integer representing the maximum difference between two elements. If such a
# solution can't be found, then print O.

# Constraints
# 0 < inputArr size < 10P
# -105 s imputArr] = 105: Where i representing the index of the inpuzArr.
# O did inputArm size

# Example

# Input;
# 7
# 23 10 6481

# Output.
# 8

# Explanation:
# The difference between 2 and 10 is 8. We can't consider 10 and 1 because the large
# number(10) does not appear after the smaller number(1).
# So, the output should be 8.


def maxDiff(arr, arr_size):
    max_diff = arr[1] - arr[0]
    min_element = arr[0]
      
    for i in range( 1, arr_size ):
        if (arr[i] - min_element > max_diff):
            max_diff = arr[i] - min_element
      
        if (arr[i] < min_element):
            min_element = arr[i]
    return max_diff