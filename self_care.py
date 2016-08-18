# dictionaries
#     .setdefault()
# recursion
# problem solving
# visualizing the problem
# details in instructions
# keeping track of the steps required to solve the problem
# using tuples
# syntax errors
# loops
#   continue
# lists
#     enumerate(iterable)
#     zip(seq1, seq2)
#     indexing
# strings
#     .split()
#     .strip()
# # sorted()/.sort() w/ key
# Example Keys:
#   len
#   operator.getitem(a, b)
#       "Return the value of a at index b."
#       See: https://docs.python.org/3.5/library/operator.html
#   get
# d = {"third": 3, "first": 1, "second": 2}
# print(sorted(d, key=d.get))

#   itemgetter
#       See: https://stackoverflow.com/questions/18595686/how-does-operator-itemgetter-and-sort-work-in-python
# # initialize
# lst = []
# # create the table (name, age, job)
# lst.append(["Nick", 30, "Doctor"])
# lst.append(["John",  8, "Student"])
# lst.append(["Paul", 22, "Car Dealer"])
# lst.append(["Mark", 66, "Retired"])
# # sort the table by age
# import operator
# lst.sort(key=operator.itemgetter(1))
# print(lst)

# names of built-in methods
# debugging
#     syntax errors
#     unexpected behavior
# formating print
# double loops
# raise
# naming variables
# = (assignment) vs. == (equality)
# not using comments/docstrings
# not modularizing code
# not testing code
#   too lazy to be exhaustive
# optimizing
# not knowing the terms (to even know what to look up)
# not developing incrementally
# # opening files
# # file read operations
#     with open syntax
# # if/then control flow
# # functions
#     function passing
#     parameters
#     arguments
# # sys.argv


# # exception handling
# `try` blocks give you a space to do something that may raise an exception
# (cause an error).
#     (1) if there is an error, deal with it in the `except` block
#     (2) if there is not an error, you can optionally use an `else` block
#     (3) `finally` can be used to catch errors from the except block and run
#     whether `try` raises an error or not.
#     (4) generally best to have as little happening in your `try` block as
# necessary
# Pattern:
# try:
#     [attempt something exception prone here]
# except:
#     [handle the exception]
# else: (optional)
#     [what to do if there is no exception]
# finally: (optional)
#     [what to do whether there is an exception or not]


#   `except Exception as e` gives you access to the exception in the `e`

# # Example 1:
# try:  # ZeroDivisionError: division by zero
#     1/0
# except Exception as e:
#     print("The variable name 'e' is your exception: {}".format(e))

# # Example 2:
# try:  # IndexError: list index out of range
#     print([1, 2][2])
# except Exception as e:
#     print("The variable name 'e' is your exception: {}".format(e))

# # Example 3
# try:  # ValueError: invalid literal for int() with base 10
#     print(int("this will not work"))
# except Exception as e:
#     print("The variable name 'e' is your exception: {}".format(e))


# # misc.
# assert
# raise
# assert

# isinstance(check_this, see_if_this)
#   returns True/False
#   test for str, int, float, list, dict, tuple, etc.
# Examples:
# isinstance([1, 2, 3], list)  # True
# isinstance(1, list)  # False

# boilerplate code
# if __name__ == "__main__":
#     main()
