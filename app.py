import os
import subprocess
import sys
import argparse

def get_commits(tag):
    """Получить список коммитов для заданного тега."""

    try:
        output = subprocess.check_output(
            ["git", "rev-list", tag],
            stderr=subprocess.STDOUT
        ).decode().strip()
        return output.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error while getting commits: {e.output.decode()}", file=sys.stderr)
        return []

def build_mermaid_graph(commits):
    """Построить граф в формате Mermaid."""
 
    graph = ["graph TD;"]
    for i, commit in enumerate(commits):
        graph.append(f"    {commit}({commit})")
        # Добавить связь только если это не последний коммит в списке
        if i < len(commits) - 1:
            graph.append(f"    {commit} --> {commits[i + 1]}")
    return "\n".join(graph)
 
def save_graph_to_file(graph, output_file):

    """Сохранить граф в файл."""
    with open(output_file, 'w') as f:
        f.write(graph)

def main():
    parser = argparse.ArgumentParser(description='Visualize commit dependencies in a Git repository.')
    parser.add_argument('repo_path', help='Path to the analyzed repository.')
    parser.add_argument('output_file', help='Path to the output file for the graph code.')
    parser.add_argument('tag', help='Tag name in the repository.')
    
    args = parser.parse_args()
    
    os.chdir(args.repo_path)  # Переход в каталог репозитория
    commits = get_commits(args.tag)
    
    if not commits:
        print("No commits found for the given tag.", file=sys.stderr)
        sys.exit(1)

    graph = build_mermaid_graph(commits)
    #print(graph)  # Вывод графа на экран
    save_graph_to_file(graph, args.output_file)

if __name__ == "__main__":
    main()
