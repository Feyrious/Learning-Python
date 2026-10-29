# Learning-Python

All lessons from the course live in the `Lessons/` folder, one file per subject:

| File | Subject |
|---|---|
| `Lessons/01-variables-and-conditions.py` | Variables, data types, `if`/`else`, `input()` and f-strings |
| `Lessons/02-loops-and-lists.py` | Lists, `for` loops, `range()`, dictionaries, tuples and sets |
| `Lessons/03-functions-and-modules.py` | Calling functions and methods, defining functions, importing modules (uses `Lessons/modules/`) |

## Branching (git-flow)

| Branch | Purpose | Created from | Merges into |
|---|---|---|---|
| `main` | Finished, stable code only. Every merge is a release | - | - |
| `develop` | Where new work is collected before a release | `main` | `main` (via a release) |
| `feature/<name>` | One new lesson or change, e.g. `feature/04-classes` | `develop` | `develop` |
| `release/<version>` | Final checks before updating `main`, e.g. `release/1.0` | `develop` | `main` and `develop` |
| `hotfix/<name>` | Urgent fix for something broken on `main` | `main` | `main` and `develop` |

### Working on a new lesson

```sh
git checkout develop
git pull
git checkout -b feature/04-classes
# ...write code and commit...
git push -u origin feature/04-classes
```

Then open a pull request into `develop`.

### Making a release

```sh
git checkout develop
git pull
git checkout -b release/1.0
git push -u origin release/1.0
```

Open a pull request from `release/1.0` into `main`. After it is merged, tag
the release and bring `main` back into `develop`:

```sh
git checkout main
git pull
git tag v1.0
git push origin v1.0
git checkout develop
git merge main
git push
```
