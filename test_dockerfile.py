"""A module imported by server.py that the Dockerfile does not COPY crash-loops the container (RES-1071, 17 Oct: analytics.py)."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))


def copied_files():
    copied = set()
    for line in open(os.path.join(HERE, "Dockerfile")):
        if line.startswith("COPY ") and not line.split()[1].endswith("/"):
            copied.update(line.split()[1:-1])
    return copied


def local_imports(path):
    """Top-level modules next to server.py that this file imports (`import a, b` and `from a import x`)."""
    src = open(path).read()
    mods = {m.strip().split(" as ")[0] for line in re.findall(r"^import (.+)$", src, re.M) for m in line.split(",")}
    mods |= set(re.findall(r"^from (\w+) import ", src, re.M))
    return {m + ".py" for m in mods if os.path.exists(os.path.join(HERE, m + ".py"))}


def test_every_local_import_is_copied():
    local = local_imports(os.path.join(HERE, "server.py"))
    assert local <= copied_files(), sorted(local - copied_files())


def test_every_module_a_copied_module_imports_is_copied_too():
    """RES-3749: backlinks.py imports backlinks_i18n.py; server.py does not, so the test above never saw it (the RES-3725 follow_link.py deploy failed the same way)."""
    seen, todo = set(), ["server.py"]
    while todo:
        f = todo.pop()
        if f in seen:
            continue
        seen.add(f)
        todo += sorted(local_imports(os.path.join(HERE, f)) - seen)
    assert seen <= copied_files(), sorted(seen - copied_files())
