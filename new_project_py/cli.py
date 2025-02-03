#!/usr/bin/env python3

import os
import argparse

PYTHON_VERSION = "3.12.8"

# Default project structure
dirs = ["notebooks", "docs"]
files = {
    ".gitignore": """
    __pycache__/
    .venv/
    *.pyc
    *.pyo
    .DS_Store
    .ruff_cache/
    """,
    "README.md": "# Project Title\n\nA short description of the project.",
    "LICENSE": "MIT License",
    "pyproject.toml": """
name = "{{project_name}}"
version = "{{version}}"
description = "In progress..."
requires-python = ">=3.12"
authors = "Peter Dresslar <peterdresslar@gmail.com>"
dependencies = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "jupyter",
    "ipykernel",
    "ipywidgets",
    ]


[tool.ruff]
target-version = "py312"
line-length = 96
exclude = ["notebooks", "docs", "tests"]

[tool.ruff.lint]
extend-select = ["E", "W", "F", "B", "I"]

# Allow longer comments
[tool.ruff.lint.pycodestyle]
max-doc-length = 100
""",
}

def create_structure(project_name):
    os.makedirs(project_name, exist_ok=True)
    for directory in dirs:
        os.makedirs(os.path.join(project_name, directory), exist_ok=True)
    for filename, content in files.items():
        with open(os.path.join(project_name, filename), "w") as f:
            f.write(content.strip() + "\n")
    print(f"✅ Project '{project_name}' initialized successfully!")

def main():
    parser = argparse.ArgumentParser(description="Initialize a new Python project with a boilerplate setup.")
    parser.add_argument("project_name", help="Name of the new project")
    args = parser.parse_args()
    create_structure(args.project_name)

if __name__ == "__main__":
    main()
