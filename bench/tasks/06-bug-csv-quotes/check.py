from lib import pytest_hidden
TEST = '''
from contacts import load_contacts
def test_quoted(tmp_path):
    p = tmp_path / "c.csv"
    p.write_text('name,email,city\\n"Doe, Jane",jane@x.com,"Austin, TX"\\nBob,bob@x.com,Oslo\\n')
    rows = load_contacts(str(p))
    assert rows == [
        {"name": "Doe, Jane", "email": "jane@x.com", "city": "Austin, TX"},
        {"name": "Bob", "email": "bob@x.com", "city": "Oslo"},
    ]
'''
def check(work, orig, answer):
    return pytest_hidden(work, TEST)
