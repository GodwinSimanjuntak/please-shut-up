def paginate(items, page, per_page=10):
    """Return the items for a 1-indexed page."""
    start = page * per_page
    return items[start:start + per_page]
