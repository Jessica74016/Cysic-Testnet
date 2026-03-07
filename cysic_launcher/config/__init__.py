"""
Cysic Testnet — Configuration module.
"""
import json
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt, Confirm

CONFIG_PATH = Path(__file__).parent / "settings.json"
console = Console(force_terminal=True)

DEFAULTS = {
    "node_type": "verifier",
    "rpc_endpoint": "https://rpc-testnet.cysic.xyz",
    "ws_endpoint": "wss://ws-testnet.cysic.xyz",
    "data_dir": "",
    "log_level": "info",
    "max_proofs_parallel": 4,
    "reward_address": "",
    "auto_update": True,
}


def load() -> dict:
    if CONFIG_PATH.exists():
        try:
            return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return dict(DEFAULTS)


def save(cfg: dict) -> None:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2), encoding="utf-8")


def interactive_setup() -> None:
    cfg = load()
    console.print("\n[bold yellow]Node Configuration[/bold yellow]\n")

    cfg["node_type"] = Prompt.ask("Node type", choices=["verifier", "prover"], default=cfg.get("node_type", "verifier"))
    cfg["rpc_endpoint"] = Prompt.ask("RPC endpoint", default=cfg.get("rpc_endpoint", DEFAULTS["rpc_endpoint"]))
    cfg["ws_endpoint"] = Prompt.ask("WebSocket endpoint", default=cfg.get("ws_endpoint", DEFAULTS["ws_endpoint"]))
    cfg["reward_address"] = Prompt.ask("Reward address (EVM)", default=cfg.get("reward_address", ""))
    cfg["max_proofs_parallel"] = int(Prompt.ask("Max parallel proofs", default=str(cfg.get("max_proofs_parallel", 4))))
    cfg["log_level"] = Prompt.ask("Log level", choices=["debug", "info", "warning", "error"], default=cfg.get("log_level", "info"))
    cfg["auto_update"] = Confirm.ask("Enable auto-update?", default=cfg.get("auto_update", True))

    save(cfg)
    console.print("\n[green]Configuration saved.[/green]")
