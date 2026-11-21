from lib import pytest_hidden, code_lines
TEST = '''
from datetime import date
from report import report_daily, report_weekly, report_monthly
T = date(2026, 3, 31)
E = [{"date": date(2026, 3, d), "amount": d} for d in (1, 10, 25, 30, 31)]
def test_same():
    assert report_daily(E, T) == "Daily report\\nevents: 1\\ntotal: 31\\navg: 31.0"
    assert report_weekly(E, T) == "Weekly report\\nevents: 3\\ntotal: 86\\navg: 28.67"
    assert report_monthly(E, T) == "Monthly report\\nevents: 4\\ntotal: 96\\navg: 24.0"
    assert report_daily([], T) == "Daily report\\nevents: 0\\ntotal: 0\\navg: 0"
'''
def check(work, orig, answer):
    before, after = code_lines(orig / "report.py"), code_lines(work / "report.py")
    if after > before * 0.7:
        return False, f"report.py only went from {before} to {after} code lines"
    return pytest_hidden(work, TEST)
