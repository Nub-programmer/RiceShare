# RiceShare

A professional CLI tool for discovering and installing Linux rice profiles.

## Installation

```bash
pip install riceshare
```

## Usage

```bash
riceshare search <query>riceshare install <profile_id>riceshare info <profile_id>riceshare backupriceshare rollback <backup_id>
```

## Features

- Search for available rice profiles
- Install profiles with atomic operations
- Profile information display
- Backup and restore functionality
- Safe package management detection

## Commands

### Search
```bash
riceshare search "minimal"
```

### Install
```bash
riceshare install my-profile-idriceshare install my-profile-id --dry-run
```

### Info
```bash
riceshare info my-profile-id
```

### Backup
```bash
riceshare backup
```

### Rollback
```bash
riceshare rollback backup_2024_01_01
```

## Requirements

- Python 3.11+
- Typer
- Rich
- requests
- PyYAML
- pathlib

## Project Structure

```
riceshare/
├── pyproject.toml
├── README.md
└── riceshare/
    ├── __init__.py
    ├── cli.py
    ├── config.py
    ├── github.py
    ├── installer.py
    ├── backup.py
    ├── packages.py
    ├── utils.py
    └── main.py
```

## Development

To install in development mode:

```bash
pip install -e .
```

## License

MIT License