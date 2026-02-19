from pathlib import Path
from tempfile import NamedTemporaryFile
import yaml

def atomic_write(path: Path, content: str):
    temp_file = NamedTemporaryFile(delete=False)
    try:
        temp_file.write(content.encode())
        temp_file.close()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.replace(temp_file.name)
    finally:
        temp_file.close()