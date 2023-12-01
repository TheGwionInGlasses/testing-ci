"""Unit tests for the functions in routines.py

"""

import unittest
import os
import src.routines as routines

# Inherit from unittest.TestCase so that the class has the assert
# functionality for testing etc


class TestSort(unittest.TestCase):
    """Provides unit tests for the mysort() function.

    """
    def setUp(self):
        self.list = [2, 134, 918, 0, 74, -1]
        self.sortedlist = [-1, 0, 2, 74, 134, 918]
    
    
    def test_returns_new_list(self):
        """Check that sorting produces a new list rather than being done
        in-place.

        """
        self.assertNotEqual(routines.mysort(self.list), self.list)

    def test_sort_empty_list(self):
        """Checks whether the sort routine works on an empty list.

        """
        self.assertEqual(routines.mysort([]), [])

    def test_sort_trivial(self):
        """Checks whether the sort routine works on a list that is already
        sorted.

        """
        self.assertEqual(routines.mysort(self.sortedlist), self.sortedlist)

    def test_sort_integers(self):
        """Checks whether the sort routine can handle an unordered list of
        integers.

        """
        self.assertEqual(routines.mysort(self.list), self.sortedlist)


class TestReverse(unittest.TestCase):
    """Provides unit tests for the reverse() function

    """
    def setUp(self):
        self.listint = [1, 2, 3, 4, 5]
        self.revlistint = [5, 4, 3, 2, 1]
        
        
    def test_simple_list(self):
        """Checks the result of passing in a list of ints.

        """
        self.assertEqual(routines.reverse(self.listint), self.revlistint)

    def test_double_reverse(self):
        """Tests that calling reverse() on its result returns a list in the
        same order as the original.

        """
        self.assertEqual(routines.reverse(routines.reverse(self.listint)), self.listint)
        

    def test_empty_list(self):
        """Tests the behaviour of the function on an empty list.

        """
        self.assertEqual(routines.reverse([]), [])


class TestMedian(unittest.TestCase):
    """Tests the median() function.

    """
    def setUp(self):
        self.list = [1, 3, 2, 5, 4]
        self.median = 3

    def test_simple_list(self):
        """Checks that the output is correct for a list of integers

        """
        self.assertEqual(routines.median(self.list), 3)

    # BONUS (think about this a bit, but skip it if you're having trouble)
    def test_median_only(self):
        """A test of the behaviour of median() only. I.e., it will still
        pass if the logic of median() is correct but there is a
        bug in mysort().

        """
        self.assertEqual(self.list.index(routines.median(self.list)), 2)


class TestSumFiles(unittest.TestCase):
    """Tests that sum_files() behaves as expected. You will need to use
    setUp() and tearDown() fixtures to create and delete files.

    """

    def setUp(self):
        """Create some files to use in your tests. This will be run before
        each unit test in this group.

        """
        # Hint: `output_file = open("filename.txt", "w")` opens
        # filename.txt to be written to the disk.

        # Hint: Write a string to the file using
        # `output_file.write("A string")`
        self.test_file_one = open("test1.txt", "w")
        self.test_file_one.write("0.1\n0.99\n-0.7")
        self.test_file_two = open("test2.txt", "w")
        self.test_file_two.write("1.4\n1.4\n1.4")
        self.lineOne = 1.5
        self.lineTwo = 2.39
        self.lineThree = 0.7
        self.test_file_one.close()
        self.test_file_two.close()

    def tearDown(self):
        """Delete the input and output files used in your tests. This will be
        run after each unit test in this group.

        """
        os.remove("test1.txt")
        os.remove("test2.txt")
        # Hint: `os.remove("file.txt")` deletes file.txt from the disk
        pass

    def test_sumation(self):
        """Check that sum_files() gives the correct output.

        """
        # Hint: `input_file = open("filename.txt", "r")` opens filename.txt
        # to be read from the disk.

        # Hint: Read a line from the file using
        # `string_val = input_file.readline()`
        routines.sum_files("test1.txt", "test2.txt", "output.txt")
        outfile = open("output.txt")
        string_valOne = float(outfile.readline().strip())
        string_valTwo = float(outfile.readline().strip())
        string_valThree = float(outfile.readline().strip())
        outfile.close()
        self.assertAlmostEqual(string_valOne, self.lineOne)
        self.assertAlmostEqual(string_valTwo, self.lineTwo)
        self.assertAlmostEqual(string_valThree, self.lineThree)
        

    def test_missing_files(self):
        """Check how sum_files() behaves if given the names of input files
        which do not exist.

        """
        #self.assertRaises(IOException(), routines.sum_files("Not_exist.txt", "Neither_do_this_one.txt"))


# BONUS (if you have time)
class TestBisection(unittest.TestCase):
    """Tests that the bisection_solve() function returns the expected
    results. This time you will need to decide what sort of tests to write
    yourself.

    """
    pass


if __name__ == '__main__':
    unittest.main()
