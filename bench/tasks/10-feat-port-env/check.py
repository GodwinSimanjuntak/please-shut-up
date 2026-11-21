from lib import pytest_hidden
TEST = '''
import importlib, server
def test_env(monkeypatch):
    monkeypatch.setenv("PORT", "9000")
    importlib.reload(server)
    assert server.get_config()["port"] == 9000
def test_default(monkeypatch):
    monkeypatch.delenv("PORT", raising=False)
    importlib.reload(server)
    assert server.get_config()["port"] == 8000
'''
def check(work, orig, answer):
    return pytest_hidden(work, TEST)
