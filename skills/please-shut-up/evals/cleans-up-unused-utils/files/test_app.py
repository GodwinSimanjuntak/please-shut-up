import json
from app import build_index


def test_build_index(tmp_path, monkeypatch):
    p = tmp_path / "posts.json"
    p.write_text(json.dumps([{"title": "Hello World"}, {"title": "Second Post!"}, {"title": "x"}]))
    monkeypatch.setenv("BATCH", "2")
    assert build_index(str(p)) == [["hello-world", "second-post"], ["x"]]
