from pathlib import Path
from typing import List, Dict
import yaml

def detect_package_manager() -> str:
    """Detect the system's package manager"""
    if Path("/etc/arch-release").exists():
        return "pacman"
    elif Path("/etc/debian_version").exists():
        return "apt"
    elif Path("/etc/fedora-release").exists():
        return "dnf"
    elif Path("/etc/redhat-release").exists():
        return "yum"
    return "unknown"

def get_installed_packages() -> List[str]:
    """Get list of installed packages based on detected package manager"""
    pkg_manager = detect_package_manager()
    try:
        if pkg_manager == "pacman":
            import subprocess
            result = subprocess.run(["pacman", "-Q"], capture_output=True, text=True)
            return result.stdout.strip().split("\n")
        elif pkg_manager == "apt":
            import subprocess
            result = subprocess.run(["dpkg", "-l"], capture_output=True, text=True)
            packages = []
            for line in result.stdout.split("\n"):
                if line.startswith("ii"):
                    parts = line.split()
                    if len(parts) >= 2:
                        packages.append(parts[1])
            return packages
        return []
    except Exception:
        return []

def export_packages() -> Dict:
    """Export installed packages to a dictionary"""
    return {
        "package_manager": detect_package_manager(),
        "packages": get_installed_packages()
    }

def import_packages(package_data: Dict):
    """Import packages from a backup (placeholder for future implementation)"""
    # This would be a more complex operation requiring user confirmation
    # and careful handling to avoid breaking the system
    pass
