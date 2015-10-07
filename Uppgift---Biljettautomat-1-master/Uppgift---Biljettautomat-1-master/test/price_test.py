#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('../lib')

from ticket import ticket_price


def prices():
    global child_price, adult_price, senior_price
    child_price = 10
    adult_price = 20
    senior_price = 15

@raises(TypeError)
def test_ticket_price_takes_an_age_as_argument():
    ticket_price()

@with_setup(prices())
def test_ticket_price_returns_correct_price_for_children():
    for age in range(0,18): # 0 - 17
        assert_equal(ticket_price(age), child_price)

@with_setup(prices())
def test_ticket_price_returns_correct_price_for_adults():
    for age in range(18,65): # 18 - 64
        assert_equal(ticket_price(age), adult_price)

@with_setup(prices())
def test_ticket_price_returns_correct_price_for_seniors():
    for age in range(65,121): # 65 - 120
        assert_equal(ticket_price(age), senior_price)