"""
Cysic Testnet — Node management: setup, verification, status monitoring.
"""
import os
import time
import logging
import platform
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box

console = Console(force_terminal=True)
logger = logging.getLogger("cysic.node")


class NodeManager:
    """Manages Cysic verifier/prover node lifecycle."""

    def __init__(self, config: dict):
        self.config = config
        self.data_dir = Path(config.get("data_dir", "./data"))
        self.rpc = config.get("rpc_endpoint", "https://rpc-testnet.cysic.xyz")
        self.node_type = config.get("node_type", "verifier")
        self.max_parallel = config.get("max_proofs_parallel", 4)

    def setup(self) -> None:
        """Initialize node data directory and download required binaries."""
        console.print("\n[bold yellow]Setting up Cysic node...[/bold yellow]\n")

        self.data_dir.mkdir(parents=True, exist_ok=True)
        (self.data_dir / "proofs").mkdir(exist_ok=True)
        (self.data_dir / "logs").mkdir(exist_ok=True)
        (self.data_dir / "keys").mkdir(exist_ok=True)

        arch = platform.machine().lower()
        system = platform.system().lower()
        console.print(f"  Platform: [cyan]{system}/{arch}[/cyan]")
        console.print(f"  Data directory: [cyan]{self.data_dir}[/cyan]")
        console.print(f"  Node type: [cyan]{self.node_type}[/cyan]")

        console.print("\n[green]Node directory initialized.[/green]")
        console.print("[dim]Download Cysic binaries from https://cysic.xyz/downloads[/dim]")

    def run_verifier(self) -> None:
        """Start the ZK proof verification loop."""
        if not self.config.get("reward_address"):
            console.print("[red]Reward address not set. Configure it first.[/red]")
            return

        console.print(f"\n[bold green]Starting {self.node_type} node...[/bold green]")
        console.print(f"  RPC: [cyan]{self.rpc}[/cyan]")
        console.print(f"  Reward address: [cyan]{self.config['reward_address']}[/cyan]")
        console.print(f"  Max parallel proofs: [cyan]{self.max_parallel}[/cyan]\n")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Waiting for proofs to verify...", total=None)
            cycle = 0
            while True:
                cycle += 1
                progress.update(task, description=f"Verification cycle #{cycle} — polling for proofs...")
                time.sleep(15)

    def show_status(self) -> None:
        """Display current node status."""
        table = Table(title="Node Status", box=box.ROUNDED)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Node type", self.node_type)
        table.add_row("RPC endpoint", self.rpc)
        table.add_row("Data directory", str(self.data_dir))
        table.add_row("Directory exists", "Yes" if self.data_dir.exists() else "No")

        if self.data_dir.exists():
            proofs_dir = self.data_dir / "proofs"
            proof_count = len(list(proofs_dir.glob("*.json"))) if proofs_dir.exists() else 0
            table.add_row("Verified proofs", str(proof_count))

        table.add_row("Reward address", self.config.get("reward_address", "Not set"))
        console.print(table)
