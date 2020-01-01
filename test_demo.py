import pytest


def func(x):
    return x + 1


def test_answer():
    '''case: test func'''
    print("test_answer func")
    assert func(3) == 4


def test_demo():
    '''case: test 'hello' in a '''
    print("test_demo test 'hello' in a")
    a = "hello world"
    assert "hello" in a

if __name__ == '__main__':
    pytest.main(["-s", "test_demo.py"])

