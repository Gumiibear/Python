#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('../lib')


from listcounts import median




@raises(TypeError)
def test_median_takes_a_list_as_argument():

    median()

def test_empty_list_should_give_0():

    assert_equal(median([]), 0)


def test_median_a_list_with_3_7_5_should_give_5():

    assert_equal(median([3, 7, 5]), 5)


def test_median_a_list_with_3_7_5_6_should_give_5_point_5():

    assert_equal(median([3, 7, 5, 6]), 5.5)


def test_median_a_list_with_3__5_should_give_4():

    assert_equal(median([5,3]), 4)


def test_median_a_list_with_3_should_give_():

    assert_equal(median([3]), 3)