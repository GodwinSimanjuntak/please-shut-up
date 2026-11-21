def add_tag(post, tag, tags=[]):
    tags.append(tag)
    post["tags"] = tags
    return post


def make_post(title, *tags):
    post = {"title": title}
    for t in tags:
        add_tag(post, t, post.get("tags", []))
    return post
