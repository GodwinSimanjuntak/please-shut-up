from lib import pytest_hidden
TEST = '''
import pytest
from signup import signup
@pytest.mark.parametrize("bad", ["nope", "a@", "@b.com", "a b@c.com", ""])
def test_bad(bad):
    with pytest.raises(ValueError):
        signup(bad, "longenough")
def test_good():
    assert signup("ada@example.com", "longenough") is True
def test_password_still_checked():
    with pytest.raises(ValueError):
        signup("ada@example.com", "short")
'''
def check(work, orig, answer):
    return pytest_hidden(work, TEST)
