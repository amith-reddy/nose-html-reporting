import unittest
from nose.exc import SkipTest


class TestMainCase(unittest.TestCase):
    def test_a(self):
        self.assertTrue(1)

    def test_b(self):
        self.assertTrue(0, "Some details")


class TestSecondCase(unittest.TestCase):
    def test_a(self):
        self.assertTrue(1)

    def test_b(self):
        self.assertTrue(1)


def test_a():
    assert 1


def test_b():
    raise RuntimeError("Some other details")


def test_c():
    raise SkipTest('skipped')


def test_1():
    print("Hello, world!")
    assert False


class TestFailedSetupCase(unittest.TestCase):
    def setUp(self):
        print("Hello, world!")
        raise Exception("bad")

    def test_whatever(self):
        pass
