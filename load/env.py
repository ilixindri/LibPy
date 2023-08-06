
"""
"""

from dotenv import load_dotenv
load_dotenv()
import os
for key, value in os.environ.items():
    try:
        __builtins__[key] = eval(value)
    except SyntaxError as e:
        __builtins__[key] = value
    except NameError as e:
        __builtins__[key] = value