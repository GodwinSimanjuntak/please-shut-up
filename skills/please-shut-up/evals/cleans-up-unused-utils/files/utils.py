import os
import re
import json
import hashlib
from datetime import datetime


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def slugify_v2(text):
    # new version, use this one
    return slugify(text)


def legacy_slugify(text):
    return text.lower().replace(" ", "_")


def read_json(path):
    with open(path) as f:
        return json.load(f)


def write_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f)


def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def format_ts(ts):
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")


def get_env(name, default=None):
    value = os.environ.get(name)
    if value is None:
        return default
    return value


class Config:
    """Old config wrapper, replaced by settings.py"""

    def __init__(self, path):
        self.data = read_json(path)

    def get(self, key, default=None):
        return self.data.get(key, default)


def chunk(items, size):
    return [items[i:i + size] for i in range(0, len(items), size)]
