from pathlib import Path
from pydantic import BaseModel
from typing import Optional, Dict
import yaml

CONFIG_DIR = Path.home() / ".riceshare"
CONFIG_FILE = CONFIG_DIR / "config.yaml"

class Profile(BaseModel):
    id: str
    name: str
    description: str
    author: str
    last_updated: str
    url: str

class Config(BaseModel):
    profiles: Dict[str, Profile]

    def get_profile(self, profile_id: str) -> Optional[Profile]:
        return self.profiles.get(profile_id)

def load_config() -> Config:
    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(parents=True)
    if not CONFIG_FILE.exists():
        CONFIG_FILE.write_text(yaml.dump({"profiles": {}}))
    with open(CONFIG_FILE, "r") as f:
        data = yaml.safe_load(f)
    return Config(**data)

def save_config(config: Config):
    with open(CONFIG_FILE, "w") as f:
        yaml.safe_dump(config.dict(), f)
