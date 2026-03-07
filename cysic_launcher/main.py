#!/usr/bin/env python3
"""
Cysic Testnet Node Manager — setup, configure, and monitor
Cysic ZK proof verification nodes on the testnet.
"""
import os
import sys
import json
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.text import Text
from rich import box

from utils import ensure_env

PROJECT_ROOT = Path(__file__).resolve().parent
CONFIG_PATH = PROJECT_ROOT / "config" / "settings.json"

console = Console(force_terminal=True)

LOGO = r"""
   _____          _        _______        _              _    
  / ____|        (_)      |__   __|      | |            | |   
 | |    _   _ ___ _  ___     | | ___  ___| |_ _ __   ___| |_  
 | |   | | | / __| |/ __|    | |/ _ \/ __| __| '_ \ / _ \ __| 
 | |___| |_| \__ \ | (__     | |  __/\__ \ |_| | | |  __/ |_  
  \_____\__, |___/_|\___|    |_|\___||___/\__|_| |_|\___|\__| 
         __/ |                                                
        |___/
"""


def load_config() -> dict:
    if CONFIG_PATH.exists():
        try:
            return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {
        "node_type": "verifier",
        "rpc_endpoint": "https://rpc-testnet.cysic.xyz",
        "ws_endpoint": "wss://ws-testnet.cysic.xyz",
        "data_dir": str(PROJECT_ROOT / "data"),
        "log_level": "info",
        "max_proofs_parallel": 4,
        "reward_address": "",
        "auto_update": True,
    }


def save_config(cfg: dict) -> None:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2), encoding="utf-8")


def show_banner() -> None:
    console.print(Text(LOGO, style="bold cyan"))
    console.print(Panel(
        "[bold]Cysic Testnet Node Manager[/bold]\n"
        "Setup, configure, and monitor ZK proof verification nodes",
        border_style="cyan",
    ))


def menu_install() -> None:
    console.print("\n[bold yellow]Installing dependencies...[/bold yellow]\n")
    req = PROJECT_ROOT / "requirements.txt"
    if req.exists():
        os.system(f'"{sys.executable}" -m pip install -r "{req}"')
        console.print("[green]Dependencies installed.[/green]")
    else:
        console.print("[red]requirements.txt not found.[/red]")


def menu_configure() -> None:
    from config import interactive_setup
    interactive_setup()


def menu_node_setup() -> None:
    from node import NodeManager
    cfg = load_config()
    mgr = NodeManager(cfg)
    mgr.setup()


def menu_run_verifier() -> None:
    from node import NodeManager
    cfg = load_config()
    mgr = NodeManager(cfg)
    try:
        mgr.run_verifier()
    except KeyboardInterrupt:
        console.print("\n[yellow]Verifier stopped.[/yellow]")


def menu_status() -> None:
    from node import NodeManager
    cfg = load_config()
    mgr = NodeManager(cfg)
    mgr.show_status()


def menu_view_config() -> None:
    cfg = load_config()
    table = Table(title="Node Configuration", box=box.ROUNDED)
    table.add_column("Parameter", style="cyan")
    table.add_column("Value", style="green")
    for k, v in cfg.items():
        table.add_row(k, str(v))
    console.print(table)


def menu_about() -> None:
    console.print(Panel(
        "[bold]Cysic Testnet Node Manager[/bold]\n\n"
        "Cysic is a ZK proof verification layer that enables\n"
        "decentralized verification of zero-knowledge proofs.\n\n"
        "[cyan]Features:[/cyan]\n"
        "  - Automated node setup and configuration\n"
        "  - ZK proof verification (verifier mode)\n"
        "  - Proof generation (prover mode)\n"
        "  - Real-time node status monitoring\n"
        "  - Reward tracking and claim management\n"
        "  - Auto-update support\n\n"
        "[dim]https://cysic.xyz[/dim]",
        title="About", border_style="cyan",
    ))


@ensure_env
def main() -> None:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        show_banner()

        console.print("[bold cyan]  Main Menu[/bold cyan]\n")
        console.print("  [cyan][1][/cyan] Install dependencies")
        console.print("  [cyan][2][/cyan] Configure node")
        console.print("  [cyan][3][/cyan] Node setup (download binaries)")
        console.print("  [cyan][4][/cyan] Run verifier")
        console.print("  [cyan][5][/cyan] View node status")
        console.print("  [cyan][6][/cyan] View configuration")
        console.print("  [cyan][7][/cyan] About")
        console.print("  [cyan][0][/cyan] Exit\n")

        choice = Prompt.ask("Select option", choices=["0","1","2","3","4","5","6","7"], default="0")

        if choice == "1":
            menu_install()
        elif choice == "2":
            menu_configure()
        elif choice == "3":
            menu_node_setup()
        elif choice == "4":
            menu_run_verifier()
        elif choice == "5":
            menu_status()
        elif choice == "6":
            menu_view_config()
        elif choice == "7":
            menu_about()
        elif choice == "0":
            console.print("[bold cyan]Shutting down. Goodbye![/bold cyan]")
            break

        Prompt.ask("\n[dim]Press Enter to continue...[/dim]", default="")


if __name__ == "__main__":
    main()
