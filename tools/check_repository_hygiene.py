"""Fail if excluded material is tracked or reintroduced by merging old history."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PREFIXES = ('submission/_video/edgeprof/', 'submission/_video/edgeprof2/', 'submission/_video/shotprof/')
FILES = ()

def forbidden(path):
    return any(path.startswith(prefix) for prefix in PREFIXES) or path in FILES or any(part.lower() in {"edgeprof", "edgeprof2", "shotprof"} for part in path.split("/"))

def git_paths(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), "-c", "core.quotepath=false", *args]).decode("utf-8").splitlines()

tracked = git_paths("ls-files")
history = git_paths("log", "--all", "--format=", "--name-only")
bad = sorted({p for p in tracked + history if p and forbidden(p)})
if bad:
    print("Repository hygiene failed: excluded file paths remain in tracked files/history:")
    print("\n".join(bad[:20]))
    sys.exit(1)
print("Repository hygiene passed: tracked files and reachable history are clean.")
