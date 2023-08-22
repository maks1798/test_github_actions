import pytest
from script_to_test import do_stuff


def test_do_stuff():
    assert do_stuff(1, 1) == 1
    # assert do_stuff(1, 2) == 1
    # assert do_stuff(2, 2) == 4
    # assert do_stuff(1, 0) == 1
    # assert do_stuff(0, 0) == 1