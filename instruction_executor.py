from typing import List
from instruction import Instruction, InstrType

class InstructionExecutor:
    '''
        execute takes an instruction and a state, and a pair containing the
        next instruction index and an updated state.
    '''
    @staticmethod
    def execute(instr: Instruction, state: List[int]) -> (int, List[int]):
        label: int = instr.i
        if instr.type == InstrType.INCR:
            # Instruction of form Rn+ -> Li
            state[instr.n] += 1
        elif instr.type == InstrType.DECR:
            # Instruction of form Rn- -> Li, Lj
            if state[instr.n] > 0:
                state[instr.n] -= 1
            else:
                label = instr.j
        
        return (label, state)
            
            