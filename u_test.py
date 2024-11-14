import unittest
from app import get_commits, build_mermaid_graph

class TestDependencyVisualizer(unittest.TestCase):
    
    def test_get_commits(self):
        # Здесь можно добавить тесты для проверки получения коммитов
        # Например, создать временный git-репозиторий и проверить
        pass
    
    def test_build_mermaid_graph(self):
        commits = ['commit1', 'commit2', 'commit3']
        expected_output = (
            "graph TD;\n"
            "    commit1(commit1)\n"
            "    commit1 --> commit2\n"
            "    commit2(commit2)\n"
            "    commit2 --> commit3\n"
            "    commit3(commit3)"
        )
        result = build_mermaid_graph(commits)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
