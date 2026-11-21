import json
from lib import sh
def check(work, orig, answer):
    code, out = sh("python3 cli.py --json --min 80", work)
    try:
        ok = json.loads(out) == {"alice": 91, "carol": 85}
    except Exception:
        return False, "--json output is not valid JSON: " + out[:100]
    if not ok:
        return False, "wrong JSON: " + out[:100]
    _, before = sh(f"python3 {orig}/cli.py", work)
    _, now = sh("python3 cli.py", work)
    return (before == now, "default table unchanged" if before == now else "default output changed")
