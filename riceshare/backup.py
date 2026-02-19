from pathlib import Path
from shutil import copytree
from riceshare.config import load_config
from riceshare.utils import atomic_write

BACKUP_DIR = Path.home() / ".riceshare-backups"

def create_backup():
    config = load_config()
    backup_path = BACKUP_DIR / f"backup_{config.profiles.keys()}.yaml"

    try:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        atomic_write(backup_path, config.dict())
        return True
    except Exception as e:
        raise RuntimeError(f"Backup failed: {str(e)}")

def rollback(backup_id: str):
    backup_path = BACKUP_DIR / f"backup_{backup_id}.yaml"
    if not backup_path.exists():
        raise FileNotFoundError(f"Backup {backup_id} not found")

    try:
        with open(backup_path, "r") as f:
            backup_data = yaml.safe_load(f)
        config = Config(**backup_data)
        save_config(config)
        return True
    except Exception as e:
        raise RuntimeError(f"Rollback failed: {str(e)}")