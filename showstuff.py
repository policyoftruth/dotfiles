import os
import sys

value = str(os.environ['ARM_VAR'])
value_list = list(value)
value_list[1] = "^"
print("The value is:")
print(value, file = sys.stderr)
print("".join(value_list))
