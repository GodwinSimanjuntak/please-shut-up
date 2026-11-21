from lib import pytest_hidden
TEST = open(__file__.replace("check.py", "repo/test_all.py")).read()
def check(work, orig, answer):
    return pytest_hidden(work, TEST)
