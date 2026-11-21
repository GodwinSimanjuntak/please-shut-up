def title_case(s):
    return " ".join(w.capitalize() for w in s.split(" "))


def truncate(s, n):
    """Cut s to at most n chars, ending with '...' if cut."""
    if len(s) <= n:
        return s
    return s[:n] + "..."
