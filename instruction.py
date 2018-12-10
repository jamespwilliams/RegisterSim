from enum import Enum
import re

class InstrType(Enum):
    HALT = 0
    DECR = 1
    INCR = 2

class Instruction:
    '''
    Instruction must be of form:
        Rn+ -> Li
        Rn- -> Li, Lj
        HALT
    '''
    instr_pattern: str = 'R?([0-9]+)([\+\-])\s*->\s*L?([0-9]+)\s*(?:,\s*L?([0-9]+))?'
    
    type: InstrType = InstrType.HALT
    n: int
    i: int
    j: int
    
    def __init__(self, instr_str):
        if instr_str == 'HALT':
            return
        
        m = re.match(self.instr_pattern, instr_str)
        if not m:
            raise ArgumentException('Invalid instruction format.')
            return
        
        self.n = int(m.group(1))
        self.i = int(m.group(3))
        if m.group(2) == '-':
            self.type = InstrType.DECR
            self.j = int(m.group(4))  
        else:
            self.type = InstrType.INCR      
        