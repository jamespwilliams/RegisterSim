from typing import List
from instruction import Instruction, InstrType

class InstructionExecutor:
    '''
        execute takes an instruction and a state, and a pair containing the
        next instruction index and an updated state.
    '''
    @staticmethod
    def execute(instr: Instruction, state: List[int]) -> (int, List[int]):
        label: int = 0
        if instr.type == InstrType.INCR:
            # Instruction of form Rn+ -> Li
            state[instr.n] += 1
            label = instr.i
        elif instr.type = InstrType.DECR:
            # Instruction of form Rn- -> Li, Lj
            label = instr.j
            if state[instr] > 0:
                state[instr] -= 1
                label = instr.i
        
        return (label, state)
            
            