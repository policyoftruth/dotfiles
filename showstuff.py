import os
import sys

value = str(os.environ['ARM_VAR'])
secretsgobrrr = str(os.environ['RECURSION'])
value_list = list(value)
value_list[1] = "^"
print("The value is:")
print(value, file = sys.stderr)
print("".join(value_list))
print("HelloProd")
print("HelloProd1")
print("*********")
print(secretsgobrrr)
