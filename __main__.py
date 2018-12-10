import sys

if (sys.version_info < (3, 5)):
    print("This module requires python 3.5.x or above.")
    exit()

if "--help" in sys.argv:
    print("Usage: `python {} program_name state`".format(sys.argv[0]))
    print("""
    program_name:
        Name of a register instruction program file.
        The passed program file must be of the correct format, with
        each line of the file being a valid register instruction. Valid
        instruction types are as follows:
            Rn+ -> Li
            Rn- -> Li, Lj
            HALT
        Separate instructions must be placed on new lines. Note that line 
        numbers are not necessary and should be omitted.
        
    state:
        A list of integers [x0, x1, ..., xn], such that registers will be
        set to R0 = x0, R1 = x1, ..., Rn = xn on program start.
        Note that the line number is not included, and will always be
        assumed to be 0.
    """)
    exit()

if len(sys.argv) < 3:
    print("Usage: `python {} program_name state`".format(sys.argv[0]))
    print("Run `python {} --help` for more".format(sys.argv[0]))
    exit()
    
import ast
from program import Program
    
p = Program()
# Safely decode the user's passed state:
state = ast.literal_eval(sys.argv[2])
p.load_from_file(sys.argv[1])

print(p.execute(state))
