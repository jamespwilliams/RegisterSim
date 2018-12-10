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
    instr_pattern: str = 
        'R?([0-9]+)([\+\-])\s*->\s*L?([0-9]+)\s*(?:,\s*L?([0-9]+))?'
    
    type: InstrType = HALT
    n: int
    i: int
    j: int
    
    def __init__(self, instr_str):
        if instr_str == 'HALT':
            return
        
        m = re.match(, statement )
        
        instr_str = re.sub('[ a-zA-Z]', '', instr_str)
        if not instr_str:
            return
            
        if '+' in instr_str:
            type = INCR
            

        
        