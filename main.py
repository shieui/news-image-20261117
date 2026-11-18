"""Copy the finished news poster to the output directory.

The entry image (entry.png, drawn at build time) sits next to this file.
The sandbox gives us a read-only repo and a writable output directory, so
all we do is copy the bytes, honouring MAKEFUN_OUTPUT_DIR when set.
"""
import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png missing from repo", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        print("copied file size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
