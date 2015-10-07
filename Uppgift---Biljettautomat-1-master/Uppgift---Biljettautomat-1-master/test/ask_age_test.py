#encoding: utf-8

from nose.tools import *
from mock import MagicMock
import __builtin__
import sys
sys.path.append('../lib')

from ticket import ask_age

def test_ask_age_asks_the_user_to_enter_their_age():
    __builtin__.raw_input = MagicMock()
    ask_age()
    __builtin__.raw_input.assert_called_with('Enter your age: ')

def test_ask_age_returns_the_input_age_as_an_integer():
    __builtin__.raw_input = MagicMock(return_value="3")
    assert_equal(ask_age(), 3)

    __builtin__.raw_input = MagicMock(return_value="65")
    assert_equal(ask_age(), 65)
