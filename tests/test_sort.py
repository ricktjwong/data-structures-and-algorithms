import random
import modules.selection_sort as ss
import modules.insertion_sort as ist


def test_selection_sort():
    A = [random.randrange(1, 1000) for i in range(100)]
    sorted_list = ss.selection_sort(A, 100)
    A.sort()
    assert (A == sorted_list)


def test_insertion_sort():
    A = [random.randrange(1, 1000) for i in range(100)]
    sorted_list = ist.insertion_sort(A, 100)
    A.sort()
    assert (A == sorted_list)
