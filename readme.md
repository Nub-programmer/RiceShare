Readme 
"We are starting fresh.

We are building ONLY the CLI. which i willl publish to pypi so make sure it looks profesional

No website.
No dashboard.
No frontend.
No monorepo.
No templates.

Repository:
https://github.com/Nub-programmer/RiceShare

This must be a clean standalone Python CLI tool.

Project name: riceshare

Goal:
A CLI tool to discover and install Linux rice profiles.

Profiles source:
https://raw.githubusercontent.com/Nub-programmer/riceshare-profiles/main/index.json

Final required structure:

RiceShare/
│
├── pyproject.toml
├── README.md
└── riceshare/
├── init.py
├── cli.py
├── config.py
├── github.py
├── installer.py
├── backup.py
├── packages.py
├── utils.py
└── main.py

Requirements:

Python 3.11+

Typer

Rich

requests

PyYAML

pathlib

Commands:

riceshare search

riceshare info <profile>

riceshare install <profile> --dry-run

riceshare rollback <backup_id>

Must include:

Proper error handling for missing index.json

Clean GitHub fetching logic

Safe backup system using ~/.riceshare

Atomic file writes

Clean CLI UX using Rich

Proper entry point in pyproject.toml

pyproject.toml must contain:

[project.scripts]
riceshare = "riceshare.cli:app"

IMPORTANT:

Do not generate any frontend files.
Do not generate index.html.
Do not generate React.
This is CLI only.

Production quality code.
No placeholders.
No mock logic.

Start by printing final structure, then full implementation." 

