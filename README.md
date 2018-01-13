todoist-cli
===========

A command line interface for adding tasks to Todoist.

## Installation
```bash
pip install todoist-cli
```

## Usage
```
Usage: todoist.py [OPTIONS] FILE

  Add tasks from a file

Options:
  -po, --project TEXT   a project id
  -pi, --priority TEXT  priority (1 to 4, 4 highest)
  -i, --indent TEXT     indent level (1 to 4, 1 top-level)
  -d, --date TEXT       due date (Todoist-formatted date string)
  --help                Show this message and exit.
```

Add four tabs to the start of a line to increment the indent level by 1.