def prune_expired(sessions, now):
    """Remove expired sessions in place and return the dict."""
    for sid, s in sessions.items():
        if s["expires"] < now:
            del sessions[sid]
    return sessions
