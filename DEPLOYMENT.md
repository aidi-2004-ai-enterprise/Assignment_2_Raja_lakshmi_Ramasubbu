##  Unit Testing Summary

All unit tests were successfully implemented and passed.

### Tests Implemented:
-  Valid prediction with known penguin data
-  Missing field (e.g., body_mass_g)
-  Invalid data types (e.g., "invalid" string for numeric)
-  Out-of-range value (e.g., negative body mass)
-  Empty request body

### Test Coverage:
Achieved **91%** test coverage on `main.py` using `pytest-cov`.

Command used:
```bash
$env:PYTHONPATH = "."
pytest --cov=app tests/
