from typer import Typer, Option, Argument
from rich.console import Console
from riceshare.config import load_config
from riceshare.github import fetch_profiles
from riceshare.installer import install_profile
from riceshare.backup import create_backup

app = Typer(app_name="riceshare", help="RiceShare CLI tool")

@app.command()
def search(query: str = Option(..., help="Search query for profiles"), dry_run: bool = Option(False, help="Dry run mode")):
    """Search for rice profiles matching the query"""
    profiles = fetch_profiles(query)
    console = Console()
    console.print(f"[bold green]Found {len(profiles)} profiles[/bold green]")
    for profile in profiles:
        console.print(f"[cyan]{profile.id}[/cyan] - {profile.name}")

@app.command()
def install(profile_id: str = Argument(..., help="Profile ID to install"), dry_run: bool = Option(False, help="Dry run mode")):
    """Install a rice profile"""
    success = install_profile(profile_id, dry_run=dry_run)
    if success:
        console = Console()
        console.print(f"[bold green]Profile {profile_id} installed successfully[/bold green]")
    else:
        console = Console()
        console.print(f"[bold red]Installation failed[/bold red]")

@app.command()
def info(profile_id: str = Argument(..., help="Profile ID to show info for")):
    """Show profile information"""
    profile = load_config().get_profile(profile_id)
    if not profile:
        console = Console()
        console.print(f"[bold red]Profile {profile_id} not found[/bold red]")
        return
    console = Console()
    console.print(f"[bold]{profile.name}[/bold]")
    console.print(f"[dim]{profile.description}[/dim]")
    console.print(f"[cyan]Author:[/cyan] {profile.author}")
    console.print(f"[cyan]Last Updated:[/cyan] {profile.last_updated}")

@app.command()
def backup():
    """Create a backup of all profiles"""
    success = create_backup()
    if success:
        console = Console()
        console.print(f"[bold green]Backup created successfully[/bold green]")
    else:
        console = Console()
        console.print(f"[bold red]Backup failed[/bold red]")

if __name__ == "__main__":
    app()