import unittest
from instruction import Instruction, InstrType

class TestInstruction(unittest.TestCase):
    def setUp(self):
        pass

    def test_halt(self):
        instr: Instruction = Instruction("HALT")
        self.assertEqual(instr.type, InstrType.HALT)

    def test_increment(self):
        instr: Instruction = Instruction("R13+ -> L12")
        self.assertEqual(instr.type, InstrType.INCR)
        self.assertEqual(instr.n, 13)
        self.assertEqual(instr.i, 12)
        
    def test_decrement(self):
        instr: Instruction = Instruction("R5- -> L2, L3")
        self.assertEqual(instr.type, InstrType.DECR)
        self.assertEqual(instr.n, 5)
        self.assertEqual(instr.i, 2)
        self.assertEqual(instr.j, 3)

if __name__ == '__main__':
    unittest.main()