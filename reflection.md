### Reflection

**1. Easiest vs Hardest Fixes**
- *Easiest:* Replacing mutable default arguments and using `with open()` for files.
- *Hardest:* Adding proper exception handling and full input validation while keeping logic clean.

**2. False Positives**
- Pylint reported naming‐style and global‐statement warnings which were not real logic bugs, just convention reminders.

**3. Integration into Workflow**
- I would integrate Pylint, Bandit, and Flake8 into a GitHub Actions CI pipeline so every push runs static checks automatically.
- During local development, I’d use a pre-commit hook to run `black`, `flake8`, and `pylint`.

**4. Improvements Observed**
- Code readability improved due to consistent style and docstrings.
- Security strengthened after removing `eval()` and broad `except`.
- Using logging and validation made the program more robust and maintainable.
