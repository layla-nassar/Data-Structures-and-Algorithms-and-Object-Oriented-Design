import math
from enum import Enum

INVERSION_BOUND = 10  # pre-defined constant; independent of list input sizes


class MagicCase(Enum):
    GENERAL = 0
    SORTED = 1
    CONSTANT_NUM_INVERSIONS = 2
    REVERSE_SORTED = 3


def linear_scan(L):
    """
    Determines the MagicCase for a given list, returning the appropriate MagicCase for each type of list.
    """
    inversion_count = sum(1 for i in range(1, len(L)) if L[i - 1] > L[i])

    if inversion_count == 0:
        return MagicCase.SORTED
    elif inversion_count == len(L) - 1:
        return MagicCase.REVERSE_SORTED
    elif inversion_count <= INVERSION_BOUND:
        return MagicCase.CONSTANT_NUM_INVERSIONS
    else:
        return MagicCase.GENERAL



def reverse_list(L, alg_set=None):
    """Reverses the input list in place efficiently using O(n) time and O(1) memory overhead.
    Args:
    L (list): The input list to be reversed.
    Returns: list: The reversed list."""
    left = 0
    right = len(L) - 1

    while left < right:
        # Swap elements at left and right indices
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return L


def magic_insertionsort(L, left, right, alg_set=None):
    """Sorts the list using Insertion Sort and checks the results of the algorithm using alg_set"""
    # Ensure left and right indices are within the bounds of the list
    if left < 0 or right > len(L):
        raise ValueError(
            "Left and right indices must be within the bounds of the list."
        )

    # Usage of insertion sort
    for i in range(left + 1, right):
        key = L[i]
        j = i - 1
        while j >= left and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key

    # Check if the sublist has at most a constant number of inversions
    if alg_set is not None and MagicCase.CONSTANT_NUM_INVERSIONS not in alg_set:
        inverted_count = sum(1 for i in range(left + 1, right) if L[i - 1] > L[i])
        if inverted_count <= INVERSION_BOUND:
            alg_set.add(MagicCase.CONSTANT_NUM_INVERSIONS)

    return L


def magic_mergesort(L, left, right):
    """
    Sorts the sublist of the input list using merge sort algorithm.

    Args:
        L (list): The input list.
        left (int): The left index of the sublist to be sorted.
        right (int): The right index of the sublist to be sorted.

    Returns:
        list: The sorted sublist.
    """
    def merge(left_sublist, right_sublist):
        """
        Merges two sorted sublists into a single sorted list.

        Args:
            left_sublist (list): The sorted left sublist.
            right_sublist (list): The sorted right sublist.

        Returns:
            list: The merged sorted list.
        """
        merged_list = []
        i = j = 0

        # Merge the elements of the left and right sublists in sorted order
        while i < len(left_sublist) and j < len(right_sublist):
            if left_sublist[i] <= right_sublist[j]:
                merged_list.append(left_sublist[i])
                i += 1
            else:
                merged_list.append(right_sublist[j])
                j += 1

        # Append the remaining elements of the left and right sublists
        merged_list.extend(left_sublist[i:])
        merged_list.extend(right_sublist[j:])

        return merged_list

    # Check if the size of the sublist is small enough to use insertion sort
    if right - left <= 20:
        magic_insertionsort(L, left, right)
        return L[left:right]

    # Calculate the mid index to divide the sublist into two halves
    mid = (left + right) // 2

    # Recursively sort the left and right halves
    left_sublist = magic_mergesort(L, left, mid)
    right_sublist = magic_mergesort(L, mid, right)

    # Merge the sorted left and right sublists
    return merge(left_sublist, right_sublist)


def magic_quicksort(L, left, right, depth=0, alg_set=None):
    """
    Sorts the sublist of the input list using quicksort algorithm.

    Args:
        L (list): The input list.
        left (int): The left index of the sublist to be sorted.
        right (int): The right index of the sublist to be sorted.
        depth (int, optional): The current recursion depth. Defaults to 0.
        alg_set (set, optional): A set to track the algorithmic results. Defaults to None.

    Returns:
        MagicCase: The MagicCase enum value representing the characteristics of the sorted sublist.
                   Possible values are MagicCase.GENERAL and MagicCase.SORTED.
    """
    if alg_set is None:
        alg_set = set()

    # Check if the size of the sublist is small enough to use insertion sort
    if right - left <= 20:
        magic_insertionsort(L, left, right, alg_set)
        return MagicCase.SORTED

    # Calculate the best-case maximum depth for quicksort
    best_case_depth = math.ceil(math.log2(right - left)) + 1

    # Check if the depth exceeds twice the best-case maximum depth
    if depth > 2 * best_case_depth:
        magic_mergesort(L, left, right)
        return MagicCase.SORTED

    # Partition the sublist using the last element as pivot
    pivot_index = right - 1
    pivot_value = L[pivot_index]
    i = left - 1
    for j in range(left, right):
        if L[j] <= pivot_value:
            i += 1
            L[i], L[j] = L[j], L[i]
    pivot_index = i + 1

    # Recursively sort the left and right partitions
    magic_quicksort(L, left, pivot_index, depth + 1, alg_set)
    magic_quicksort(L, pivot_index + 1, right, depth + 1, alg_set)

    # Check if the sublist is sorted after quicksort
    if all(L[k] <= L[k + 1] for k in range(left, right - 1)):
        return MagicCase.SORTED
    else:
        return MagicCase.GENERAL


def magicsort(L):
    """
    Sorts the input list using a hybrid sorting algorithm.

    Args:
        L (list): The input list.

    Returns:
        set: A set containing the names of the sub-algorithms invoked during the sorting process.
    """
    # Call linear_scan to determine the characteristics of the input list
    case = linear_scan(L)

    # If the input list falls into certain cases, apply linear time sorting methods
    if (
        case == MagicCase.SORTED
        or case == MagicCase.REVERSE_SORTED
        or case == MagicCase.CONSTANT_NUM_INVERSIONS
    ):
        return set()
    elif case == MagicCase.GENERAL:
        # Call magic_quicksort on the entire list
        alg_set = set()
        magic_quicksort(L, 0, len(L), alg_set=alg_set)
        return alg_set




