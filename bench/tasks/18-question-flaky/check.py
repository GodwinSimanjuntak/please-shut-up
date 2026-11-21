import re
from lib import unchanged
def check(work, orig, answer):
    if not unchanged(work, orig):
        return False, "files were modified"
    a = answer.lower()
    ok = "set" in a and re.search(r"order", a)
    return bool(ok), "explains set ordering" if ok else "doesn't name set ordering as the cause"
