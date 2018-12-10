from typing import List
from instruction import Instruction, InstrType
from instruction_executor import InstructionExecutor

class Program:
    instructions: List[Instruction] = []
    
    def __init__(self):
        self.instructions = []
    
    def execute(self, state):
        if len(self.instructions) == 0:
            return state
        
        instr = self.instructions[0]
        while instr.type != InstrType.HALT:
            label, state = InstructionExecutor.execute(instr, state)

            if label > len(self.instructions):
                raise RuntimeError("Program jumped to invalid label.")
            
            instr = self.instructions[label]
            
        return state
        
            
    def add(self, instr_str):
        self.instructions.append(Instruction(instr_str))