import unittest
from instruction import Instruction
from instruction_executor import InstructionExecutor

class TestInstruction(unittest.TestCase):
    def setUp(self):
        pass

    def test_increment(self):
        instr: Instruction = Instruction("R1+ -> L3")
        label, state = InstructionExecutor.execute(instr, [0,0,0,0])
        self.assertEqual(label, 3)
        self.assertEqual(state, [0,1,0,0])
        
    def test_decrement_zero(self):
        instr: Instruction = Instruction("R3- -> L1, L5")
        label, state = InstructionExecutor.execute(instr, [0,0,0,0])
        self.assertEqual(label, 5)
        self.assertEqual(state, [0,0,0,0])
        
    def test_decrement_non_zero(self):
        instr: Instruction = Instruction("R3- -> L1, L5")
        label, state = InstructionExecutor.execute(instr, [0,0,0,1])
        self.assertEqual(label, 1)
        self.assertEqual(state, [0,0,0,0])
        
    def test_multiple_instructions(self):
        state = [5,2,3,1]
        instr1: Instruction = Instruction("R3- -> L1, L5")
        instr2: Instruction = Instruction("R2+ -> L1")
        
        label, state = InstructionExecutor.execute(instr1, state)
        label, state = InstructionExecutor.execute(instr1, state)
        label, state = InstructionExecutor.execute(instr2, state)
        label, state = InstructionExecutor.execute(instr1, state)
        
        self.assertEqual(label, 5)
        self.assertEqual(state, [5,2,4,0])

if __name__ == '__main__':
    unittest.main()