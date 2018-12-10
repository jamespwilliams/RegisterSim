import unittest
from instruction import Instruction
from instruction_executor import InstructionExecutor

class TestInstruction(unittest.TestCase):
    def setUp(self):
        pass

    def test_increment(self):
        instr: Instruction = Instruction("R1+ -> L3")
        label, state = InstructionExecutor.execute(instr, (0,0,0,0))
        self.assertEqual(label, 3)
        self.assertEqual(state, (0,1,0,0))
        
    def test_decrement(self):
        instr: Instruction = Instruction("R5- -> L2, L3")
        self.assertEqual(instr.n, 5)
        self.assertEqual(instr.i, 2)
        self.assertEqual(instr.j, 3)

if __name__ == '__main__':
    unittest.main()