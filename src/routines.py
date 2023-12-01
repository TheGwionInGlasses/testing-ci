"""A collection of miscellaneous helper functions which you should
write tests for. Once that is done, you can provide implementations.

"""

import statistics

def mysort(sequence):
    """Returns a copy of the input list "sequence" with items sorted in
ascending order.

    """
    return sorted(sequence)


def reverse(sequence):
    """Returns a copy of the input list "sequence" with the items in the
opposite order.

    """
    cpy = sequence.copy()
    cpy.reverse()
    return cpy


def median(sequence):
    """Using the previous mysort() function, returns the median value of a
sequence. (I.e., the "middle" value.)

    """
    return statistics.median(mysort(sequence))


def sum_files(file1, file2, outfile):
    """Read in floating point numbers from two files, line by line,
printing the sum of the two numbers to a third file.

E.g., the input files f1.txt and f2.txt below would result in output.txt:

    f1.txt:
    1.0
    2.0
    4.0

    f2.txt
    4.1
    3.2
    -11.0

    output.txt
    5.1
    5.2
    -7.0

    """
    try:
        file_one = open(file1, "r")
        file_two = open(file2, "r")
    except:
        raise IOException()
    linesOne = file_one.readlines()
    linesTwo = file_two.readlines()
    res = []
    length = len(linesOne) if len(linesOne) < len(linesTwo) else len(linesTwo)
    for x in range(length):
        res.append(float(linesOne[x]) + float(linesTwo[x]))
    str_res = ""
    for r in res:
        str_res = str_res + str(r) + '\n'
    
    of = open(outfile, "w")
    of.write(str_res)
    of.close()
    return 0.


# BONUS (if you have time)
def bisection_solve(func, lower, upper, tol=1e-5):
    """An iterative solver using the bisection method. The argument "func"
is a function of the form

    f(float x) -> float

for which to find the root. The arguments "lower" and "upper" are
values known to be below and above the root, respectively. If they do
not bracket the root then an exception should be thrown. The tolerance
to which to find the root is given by "tol".

    """
    return 0.
