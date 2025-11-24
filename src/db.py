"""
db.py - simple JSON file storage helpers
Uses atomic write to avoid partial writes.
"""
import json, os, tempfile

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

def _path(name):
    return os.path.abspath(os.path.join(DATA_DIR, name + ".json"))

def read(name):
    p = _path(name)
    if not os.path.exists(p):
        return []
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def write(name, data):
    p = _path(name)
    d = json.dumps(data, indent=2, ensure_ascii=False)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p))
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(d)
    os.replace(tmp, p)
