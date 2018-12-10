import ast
import sys
from program import Program

if len(sys.argv) < 3:
    print("Usage: python {} program_name.rprog state".format(sys.argv[0]))
    exit()

p = Program()
# Safely decode the user's passed state:
state = ast.literal_eval(sys.argv[2])
p.load_from_file(sys.argv[1])

print(p.execute(state))
