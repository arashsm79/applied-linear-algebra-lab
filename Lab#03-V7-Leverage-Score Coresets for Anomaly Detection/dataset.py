import json
import zipfile
import urllib.request
from pathlib import Path

MAKE_ZIP = True  # True -> also create bottle.zip; False -> download only

root = Path.cwd() / "bottle"
root.mkdir(parents=True, exist_ok=True)

base = "https://huggingface.co/datasets/foersben/mvtec-ad/resolve/main/"
api = "https://huggingface.co/api/datasets/foersben/mvtec-ad/tree/main/bottle?recursive=1"

with urllib.request.urlopen(api) as r:
    entries = json.load(r)

files = [e["path"] for e in entries if e["type"] == "file"]
for i, rel in enumerate(files, 1):
    out = root.parent / rel  # bottle/train/..., bottle/test/..., etc.
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        print(f"[{i}/{len(files)}] skip {rel}")
        continue
    print(f"[{i}/{len(files)}] {rel}")
    urllib.request.urlretrieve(base + rel, out)

print("download done:", root.resolve())

if MAKE_ZIP:
    zip_path = Path.cwd() / "bottle.zip"
    print(f"zipping -> {zip_path}")
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in root.rglob("*"):
            if p.is_file():
                zf.write(p, p.relative_to(root.parent))
    print("zip done:", zip_path.resolve())
