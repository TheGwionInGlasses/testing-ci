"""Contains solution for the sorting exercise. This exercise will be
completed by the instructor as an example, but this provides a
reference if needed.

"""

import unittest


def mysort(sequence):
    """Returns a copy of the input list "sequence" with items sorted in
ascending order.

Note that this "bubble sort" algorithm is quite slow and generally
should not be used.

    """
    n = len(sequence)
    new_sequence = list(sequence)
    if n < 2:
        return new_sequence
    changed = True
    count = 0
    while changed and count < n:
        changed = False
        for i in range(n - 1 - count):
            item1 = new_sequence[i]
            item2 = new_sequence[i + 1]
            if item2 < item1:
                changed = True
                new_sequence[i] = item2
                new_sequence[i + 1] = item1
        count += 1
    return new_sequence


class TestSort(unittest.TestCase):
    """Provides unit tests for the mysort() function.

    """

    def test_returns_new_list(self):
        """Check that sorting produces a new list rather than being done
        in-place.

        """
        sequence = [0, 5, 2, 11]
        copy = list(sequence)
        self.assertIsNot(sequence, mysort(sequence))
        self.assertEqual(sequence, copy)

    def test_sort_empty(self):
        """Checks whether the sort routine works on an empty list.

        """
        self.assertEqual([], mysort([]))

    def test_sort_trivial(self):
        """Checks whether the sort routine works on a list that is already
        sorted.

        """
        sequence = list(range(20))
        self.assertEqual(sequence, mysort(sequence))

    def test_sort_integers(self):
        """Checks whether the sort routine can handle an unordered list of
        integers.

        """
        sequence = [34, 2, -1, 0, 0, 1, -3, 20, 18, 27, 34, 35]
        result = [-3, -1, 0, 0, 1, 2, 18, 20, 27, 34, 34, 35]
        self.assertEqual(result, mysort(sequence))


if __name__ == '__main__':
    unittest.main()
