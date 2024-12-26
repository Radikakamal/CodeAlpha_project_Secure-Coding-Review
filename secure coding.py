# Insecure: Using eval to evaluate user input
eval(user_input)

# Secure: Use safer parsing methods
import ast
safe_input = ast.literal_eval(user_input)