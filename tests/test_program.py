import unittest
from program import Program

class TestProgram(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_program(self):
        p = Program()
        self.assertEqual(p.execute([1, 2, 3]), [1, 2, 3])
        
    def test_incrementer(self):
        p = Program()
        p.add("R0+ -> L1")
        p.add("HALT")
        
        state = p.execute([0])
        self.assertEqual(state, [1])
        
    def test_simple_program(self):
        p = Program()
        p.add("R1- -> L1, L2")
        p.add("R0+ -> L0")
        p.add("HALT")
    
        state = p.execute([0,5])
        self.assertEqual(state, [5,0])
    
    def test_broken_program(self):
        p = Program()
        p.add("R0+ -> L1")
        self.assertRaises(RuntimeError, p.execute, [0,0])
        
    def test_load_program(self):
        p = Program()
        p.load_from_file("tests/test_programs/test_prog.rprog")
        
        state = p.execute([0,5])
        self.assertEqual(state, [5,0])
        
    def test_multiplication_program(self):
        p = Program()
        p.load_from_file("tests/test_programs/mult.rprog")
        
        state = p.execute([0, 13, 5, 0, 0, 0, 0])
        self.assertEqual(state[0], 65)
        

if __name__ == '__main__':
    unittest.main()