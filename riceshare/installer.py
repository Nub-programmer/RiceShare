from pathlib import Path
from shutil import copytree, rmtree
from riceshare.config import load_config, save_config
from riceshare.utils import atomic_write

def install_profile(profile_id: str, dry_run: bool = False) -> bool:
    config = load_config()
    if profile_id not in config.profiles:
        return False

    profile = config.profiles[profile_id]
    target_dir = Path.home() / f".riceshare-profiles/{profile_id}"

    if not dry_run:
        try:
            atomic_write(target_dir / "profile.yaml", profile.dict())
            copytree(Path(__file__).parent / "templates", target_dir / "templates")
            save_config(config)
            return True
        except Exception as e:
            raise RuntimeError(f"Installation failed: {str(e)}")
    return True