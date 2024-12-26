### Issues Identified:
1. Hardcoded credentials (file: app.py, line 23).
2. Use of eval() for input evaluation (file: main.py, line 42).
3. Missing input validation for form inputs.

### Recommendations:
1. Use environment variables to store sensitive data.
2. Replace eval() with safer parsing alternatives.
3. Implement input validation using libraries like Cerberus or Marshmallow