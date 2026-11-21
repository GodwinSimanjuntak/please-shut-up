import re
from lib import pytest_hidden, code_lines
TEST = open(__file__.replace("check.py", "repo/test_app.py")).read()
def check(work, orig, answer):
    src = (work / "utils.py").read_text()
    left = [n for n in ["legacy_slugify", "write_json", "md5_file", "format_ts", "class Config"] if n in src]
    if left:
        return False, f"unused code still there: {left}"
    if re.search(r"^\s*import (hashlib|datetime)|^from datetime", src, re.M):
        return False, "unused imports still there"
    return pytest_hidden(work, TEST)
