# coding=utf_8
import pytest


def func(x):
    return x + 1


@pytest.mark.parametrize('a, b', [(1, 3), (5, 6), (10, 20)])
def test_answer(a, b):
    assert func(a) == b


@pytest.fixture()
def login():
    username = 'Jerry'
    return username


class TestDemo:
    def test_a(self, login):
        print(f"a username = {login}")

    def test_b(self):
        print("b")


if __name__ == '__main__':
    pytest.main(['test_a.py'])
