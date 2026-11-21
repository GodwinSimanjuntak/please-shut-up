from lib import pytest_hidden
TEST = '''
import pytest, time
import client
from client import fetch, TransientError

class T:
    def __init__(self, fails, exc=TransientError):
        self.fails, self.exc, self.calls = fails, exc, 0
    def get(self, url):
        self.calls += 1
        if self.calls <= self.fails:
            raise self.exc("boom")
        return "ok"

@pytest.fixture(autouse=True)
def nosleep(monkeypatch):
    monkeypatch.setattr(time, "sleep", lambda s: None)

def test_recovers():
    t = T(2); assert fetch(t, "u") == "ok"; assert t.calls == 3

def test_gives_up():
    t = T(3)
    with pytest.raises(TransientError):
        fetch(t, "u")
    assert t.calls == 3

def test_other_errors():
    t = T(1, ValueError)
    with pytest.raises(ValueError):
        fetch(t, "u")
    assert t.calls == 1
'''
def check(work, orig, answer):
    return pytest_hidden(work, TEST)
