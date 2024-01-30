"""
Author  : Spadel
Name    : graph_vis.py
Date    : 2024/01/30
"""
import os
import re

Scan_Dir = "your/project/path"
Import_Regex = r'^(?:from\s+(\S+)\s+import\s+\S+ | import\s+(\S+))'
dependencies = {}

for root,dirs,files in os.walk(Scan_Dir):
    for file in files:
        if file.endswith('.py'):
            path = os.path.join(root,file)
            with open(path,'r') as f:
                content = f.readlines()
            for line in content:
                match = re.match(Import_Regex,line)
                if match:
                    imported_module = match.group(1) or match.group(2)
                    if file not in dependencies:
                        dependencies[file] = set()
                    dependencies[file].add(imported_module)


print('digraph G {')
for file, imports in dependencies.items():
    print(f'"{file}" [shape=box];')
    for imp in imports:
        print(f'"{file}" -> "{imp}";')
print ('}')