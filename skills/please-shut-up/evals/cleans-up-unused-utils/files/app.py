from utils import slugify_v2, read_json, chunk, get_env


def build_index(path):
    posts = read_json(path)
    batch = int(get_env("BATCH", "10"))
    pages = chunk(posts, batch)
    return [[slugify_v2(p["title"]) for p in page] for page in pages]
