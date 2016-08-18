# # Checklist items:
# visualizing the problem
#   start w/ identifying the task
# details in instructions
# naming variables
# not using comments/docstrings
# not modularizing code
# not testing code
#   too lazy to be exhaustive
# read the traceback

# not developing incrementally
# keeping track of the steps required to solve the problem
#   create to do list

# optimizing
#   don't optimize too early





# # Ctrl+C to stop program, 
# #   triggers a KeyboardInterrupt exception

# #Not good pattern:
# while True:
#     try:
#         x = int(input(": "))
#     except:
#         "oops, try again"
# # If above is the code, try Ctrl+Z
# while True:
#     y = input(": ")
#     try:
#         x = int(y)
#     except:
#         "oops, try again"





# dictionaries
#     .setdefault()
# recursion
    # insert example from test
    # insert examples or links to recursions (prime, palindrome)

# using tuples
#   enumerate()
#         Ex. 1; list(enumerate(someotherlist))
#         Ex. 2: for a, b in enumerate(list)
#       Gives you a list of tuples (index, item), etc
#           the a, b above is unpacking each typle pair
#   zip()
#   returning multiple variables
# #   Example:
# def f():
#     return 1, 2  # This is called tuple packing

# a, b = f()  # This is called tuple unpacking


# syntax errors
#   https://i.imgur.com/WRuJV6r.png
#   look at the traceback
#   read what the syntax error



# loops
#   continue
#       goes to the beginning/top of loop ON the next iteration
#   break
#        leaves the loop (note: only the inner loop if there are more than one)




# lists
#     enumerate(iterable)
# list1 = ["a", "b", "c"]
# list(enumerat(list1))
# returns: :[(0, 'a'), (1, 'b'), (2, 'c')]


#     zip(seq1, seq2)

# list2 = ["z", "y", "x"]
# list(zip(list1, list2))
# #[('a', 'z'), ('b', 'y'), ('c', 'x')]



#     indexing



# strings
#     .split(defaults to white space)
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



# Reading
# names of built-in methods
#   https://docs.python.org/3/library/functions.html


# debugging  - checklist
#     syntax errors
#     unexpected behavior


# formating print
# https://docs.python.org/3.5/library/string.html


# double loops





# = (assignment) vs. == (equality)




# not knowing the terms (to even know what to look up)

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
