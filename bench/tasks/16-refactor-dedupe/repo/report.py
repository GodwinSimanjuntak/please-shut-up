from datetime import date, timedelta


def report_daily(events, today):
    start = today - timedelta(days=1)
    recent = [e for e in events if start < e["date"] <= today]
    total = sum(e["amount"] for e in recent)
    count = len(recent)
    avg = round(total / count, 2) if count else 0
    lines = ["Daily report", f"events: {count}", f"total: {total}", f"avg: {avg}"]
    return "\n".join(lines)


def report_weekly(events, today):
    start = today - timedelta(days=7)
    recent = [e for e in events if start < e["date"] <= today]
    total = sum(e["amount"] for e in recent)
    count = len(recent)
    avg = round(total / count, 2) if count else 0
    lines = ["Weekly report", f"events: {count}", f"total: {total}", f"avg: {avg}"]
    return "\n".join(lines)


def report_monthly(events, today):
    start = today - timedelta(days=30)
    recent = [e for e in events if start < e["date"] <= today]
    total = sum(e["amount"] for e in recent)
    count = len(recent)
    avg = round(total / count, 2) if count else 0
    lines = ["Monthly report", f"events: {count}", f"total: {total}", f"avg: {avg}"]
    return "\n".join(lines)
