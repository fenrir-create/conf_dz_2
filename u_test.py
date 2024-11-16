import unittest
from app import get_commits, build_mermaid_graph

class TestDependencyVisualizer(unittest.TestCase):
    
    def test_get_commits(self):
        
        pass
    
    def test_build_mermaid_graph(self):
        commits = ['75600d34d31af2c3e3a823a1f649421298efaf32', '4c20011a80a65c268086775fa4d3d52c5c03503f', 'd4f220349a97281810d373ffdc176729f218f98b']
        expected_output = (
            "graph TD;\n"
            "    75600d34d31af2c3e3a823a1f649421298efaf32(75600d34d31af2c3e3a823a1f649421298efaf32)\n"
            "    75600d34d31af2c3e3a823a1f649421298efaf32 --> 4c20011a80a65c268086775fa4d3d52c5c03503f\n"
            "    4c20011a80a65c268086775fa4d3d52c5c03503f(4c20011a80a65c268086775fa4d3d52c5c03503f)\n"
            "    4c20011a80a65c268086775fa4d3d52c5c03503f --> d4f220349a97281810d373ffdc176729f218f98b\n"
            "    d4f220349a97281810d373ffdc176729f218f98b(d4f220349a97281810d373ffdc176729f218f98b)"
        )
        result = build_mermaid_graph(commits)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
