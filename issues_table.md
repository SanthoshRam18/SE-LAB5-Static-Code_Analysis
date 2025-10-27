| Issue | Tool | Line(s) | Description | Fix |
|-------|------|---------|--------------|------|
| Mutable default argument | Pylint | 14 | Used `logs=[]` which is shared across calls | Changed default to `None` and initialized inside function |
| Bare except | Pylint/Bandit | 33 | `except:` hides all errors | Replaced with `except KeyError as err:` and added logging |
| Unsafe eval usage | Bandit | 109 | Executed arbitrary code with `eval()` | Removed completely |
| Unsafe file handling | Pylint/Flake8 | 63, 77 | Used manual open/close | Switched to `with open()` for safe file I/O |
| Missing input validation | Pylint | 20–30 | Function accepted invalid types | Added `isinstance()` checks and error logging |
| Missing docstrings & naming style | Pylint | various | Functions lacked docstrings / not in snake_case | Added proper docstrings & renamed functions |
