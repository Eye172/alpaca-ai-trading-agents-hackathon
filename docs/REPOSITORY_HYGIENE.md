# Browser-profile cleanup - 2026-10-12

Removed `submission/_video/edgeprof/`, `edgeprof2/` and `shotprof/` from every
reachable commit, branch and tag. These folders included browser cookies,
history, login stores, local storage, sessions and caches. No browser database
contents were needed for this cleanup.

All 214 original commits remain. Before adding the hygiene checks, every other
file was verified byte-for-byte against the pre-cleanup repository. Authors,
timestamps, messages and parent relationships were verified unchanged; one
original commit ID changed. Application code, application databases, paper-trading
records and submission videos were not removed by this browser-only cleanup.

The original mirror is retained locally for recovery, outside the publication
checkout. Never push that backup or merge a pre-cleanup clone into this history.
Re-clone, or transplant reviewed code changes without bringing old history back.

`docs/migration/` records the earlier import, not the current filtered tree.
Ignore rules and `python tools/check_repository_hygiene.py` guard against recurrence.
The GitHub workflow checks reachable history as well as currently tracked files.

Repository visibility is unchanged. Rewriting refs does not purge copies in other
clones or GitHub cached commit views. GitHub Support handles server-side sensitive
data removal: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
