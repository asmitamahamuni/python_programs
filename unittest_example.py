import os
import unittest

def analyze_text(filename):
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
        return(lines, chars)
        

class TestAnalysisTests(unittest.TestCase):

    def setUp(self):
        self.filename = 'test_analysis.txt'
        with open(self.filename, 'w') as f:
            f.write('this is test\n'
                    'this is test\n'
                    'this is test\n')



    def test_function_runs(self):
        analyze_text(self.filename)

    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[0], 3)

    def test_character_count(self):
        self.assertEqual(analyze_text(self.filename)[1], 39)


if __name__ == '__main__':
    unittest.main()
    
