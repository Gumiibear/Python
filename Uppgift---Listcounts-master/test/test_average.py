#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('../lib')


from listcounts import average




@raises(TypeError)
def test_average_takes_a_list_as_argument():

    average()



def test_average_a_empty_list_should_give_0():

    assert_equal(average([]), 0)


def test_average_a_list_with_3_7_5_should_give_5():

    assert_equal(average([3, 7, 5]), 5)


def test_average_a_list_with_3_7_5_6_should_give_5_point_25():

    assert_equal(average([3, 7, 5, 6]), 5.25)


def test_average_a_list_with_3__5_should_give_4():

    assert_equal(average([5, 3]), 4)


def test_average_a_list_with_3_should_give_3():

    assert_equal(average([3]), 3)


def test_average_a_list_with_3_3_4_should_give_3_point_3333333333333335():

    assert_equal(average([3,3,4]), 3.3333333333333335 )