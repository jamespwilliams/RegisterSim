from typing import List
from instruction import Instruction

class Program:
    instructions: List[Instruction]
    
    def execute(self):
        for instruction in instructions:
            instruction.execute()
            
    def add(self, instr_str):
        instructions.append(Instruction(instr_str))