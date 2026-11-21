class TransientError(Exception):
    pass


def fetch(transport, url):
    return transport.get(url)
