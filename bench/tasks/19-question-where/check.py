from lib import unchanged
def check(work, orig, answer):
    if not unchanged(work, orig):
        return False, "files were modified"
    ok = "limits.py" in answer and "100" in answer
    return ok, "names limits.py and 100/minute" if ok else "missing file or value"
