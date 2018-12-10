from typing import List
from instruction import Instruction, InstrType
from instruction_executor import InstructionExecutor

class Program:
    instructions: List[Instruction]
    
    def __init__(self):
        pass
    
    def execute(self, state):
        if len(instructions) == 0:
            return state
        
        instr = instructions[0]
        while instr.type != InstrType.HALT:
            label, state = InstructionExecutor.execute(instr, state)
            instr = instructions[label]
            
        return state
        
            
    def add(self, instr_str):
        instructions.append(Instruction(instr_str))