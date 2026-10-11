# Migration validation

Review date: 2026-10-11. Team: QwertyS.

## History preservation

Every imported commit was checked against its original object: file tree, message,
author timestamp, committer timestamp and mapped parent relationships were preserved.
All published copy commits use Shakhnazar Akhmer <260007353+Eye172@users.noreply.github.com> as both author and committer.
The original identities and original-to-republished mapping are preserved in `history.json`.
Original source histories are retained; their additional documentation commits touch only README.md.

## Content integrity

The file manifest records both the original local SHA-256 and committed SHA-256.
Source text may use normalized LF line endings. Archived challenge datasets,
submissions, working results, journal and evidence keep their original bytes.
Typical API-token and private-key text patterns were checked without exposing values.
Environment files containing credentials, process state, bytecode and dependency
installations are provided separately from source control.

## Project checks and limitations

Journal verification passed: 5,988 entries, hash chain intact. Both copied SQLite databases passed PRAGMA quick_check. The existing test suite returned 143 passed and 24 failed at the current date. A failing selector test also fails in the original local project. Tests use fixed 2026 option expirations while MockAlpacaClient prices from datetime.now(timezone.utc); the historical test suite needs an explicit clock. Runtime strategy source is unchanged by this migration. The manually dispatched heartbeat now uses Eye172 commit identity.

## Repository administration

The migration uses the existing collaborator access. Repository visibility and
settings are unchanged. Original repository snapshots are retained locally.
