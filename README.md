# Cysic-Testnet
Cysic Testnet — Automation tool for Cysic ZK hardware acceleration network testnet with node management, validator setup, proof generation monitoring, reward tracking, and Rich terminal interface for zero-knowledge proof infrastructure participation
<div align="center">

```
   _____          _        _______        _              _    
  / ____|        (_)      |__   __|      | |            | |   
 | |    _   _ ___ _  ___     | | ___  ___| |_ _ __   ___| |_  
 | |   | | | / __| |/ __|    | |/ _ \/ __| __| '_ \ / _ \ __| 
 | |___| |_| \__ \ | (__     | |  __/\__ \ |_| | | |  __/ |_  
  \_____\__, |___/_|\___|    |_|\___||___/\__|_| |_|\___|\__| 
         __/ |                                                
        |___/
```

### Terminal Launcher for Cysic Testnet Node

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue?style=for-the-badge)]()
[![Cysic](https://img.shields.io/badge/Cysic-Testnet-6C5CE7?style=for-the-badge)](https://cysic.xyz)

**Rich-styled terminal launcher** for Cysic Testnet nodes.
Configure RPC, Chain ID, node type — manage your ZK compute infrastructure from CLI.

[Getting Started](#-getting-started) · [Features](#-features) · [Configuration](#-configuration) · [Usage](#-usage) · [FAQ](#-faq)

</div>

---

## 🔗 Official Cysic Links

| Step | Link | Description |
|:----:|------|-------------|
| **1** | [Cysic Website](https://cysic.xyz) | Official homepage — ComputeFi and ZK infrastructure |
| **2** | [Cysic Docs](https://docs.cysic.xyz) | Technical documentation, node setup, and API references |
| **3** | [Cysic Network Overview](https://docs.cysic.xyz/cysic-network-overview) | Architecture, Proof-of-Compute consensus, token economics |

> Cysic is a decentralized compute infrastructure for ZK proofs, AI inference, and verifiable computation. Built on Cosmos CDK with Proof-of-Compute consensus, the network processed 10M+ ZK proofs during testnet with 260,000+ nodes globally. Mainnet launched December 2025 with $CYS token and ComputeFi framework.

---

## ⚡ Features

<table>
<tr>
<td width="50%">

**Node Management**
- ✅ Configure RPC URL and Chain ID
- ✅ Select node type (full / validator)
- ✅ Check node configuration status
- ✅ Run Node — instructions and launch
- ✅ Auto-start toggle

</td>
<td width="50%">

**CLI & Infrastructure**
- ✅ Rich-styled terminal UI (panels, tables)
- ✅ Cysic ASCII logo with styled borders
- ✅ Persistent settings (JSON config)
- ✅ Windows `run.bat` one-click launcher
- ✅ Auto dependency installation

</td>
</tr>
</table>

---

## 📦 Getting Started

### Prerequisites

- **Python 3.8** or higher ([download](https://python.org/downloads/))
- **pip** (included with Python)
- Familiarity with Cysic node requirements (see [Cysic Docs](https://docs.cysic.xyz))

### Installation

**Option A — Windows (one-click):**

Double-click `run.bat` — it installs Rich automatically and launches the menu.

**Option B — Manual (all platforms):**

```bash
git clone https://github.com/user/Cysic-Testnet.git
cd Cysic-Testnet
pip install -r requirements.txt
python cysic_launcher/main.py
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `rich` | ≥ 13.0 | Terminal UI — panels, tables, styled output |

---

## ⚙ Configuration

### `cysic_launcher/config/settings.json` — Node Settings

Configured via the Settings menu (option 2) or edit directly. Auto-created on first launch:

```json
{
  "rpc_url": "https://rpc.testnet.cysic.xyz",
  "chain_id": "cysic-testnet-1",
  "node_type": "full",
  "auto_start": false
}
```

| Setting | Description |
|---------|-------------|
| `rpc_url` | Cysic testnet RPC endpoint for node communication |
| `chain_id` | Network chain identifier (`cysic-testnet-1` for testnet) |
| `node_type` | Node role — `full` (sync and validate) or `validator` (active block production) |
| `auto_start` | Auto-launch node on application start (true/false) |

---

## 🚀 Usage

```bash
python cysic_launcher/main.py
```

Or on Windows:

```cmd
run.bat
```

The interactive menu:

```
╔══════════════════════════════════════════════════════╗
║                Cysic Testnet Launcher                 ║
║         Compute Infrastructure for ZK & AI             ║
╚══════════════════════════════════════════════════════╝

  ╭──────────────────────────────────────────────────╮
  │  1   Install Dependencies                        │
  │  2   Settings — RPC, Chain ID, Node Type         │
  │  3   About — Cysic network info                  │
  │  4   Check Status — view node configuration      │
  │  5   Run Node (Info) — launch instructions       │
  │  0   Exit                                        │
  ╰──────────────────────────────────────────────────╯

  Select option:
```

| Option | What it does |
|:------:|-------------|
| `1` | Installs `rich` from `requirements.txt` via pip |
| `2` | Interactive settings — edit RPC URL, Chain ID, node type, auto-start toggle |
| `3` | About Cysic — network overview, hashtags, documentation links |
| `4` | Displays current node configuration (RPC, chain, type) from settings |
| `5` | Shows instructions for running a Cysic testnet node with current config |
| `0` | Exit the application |

---

## 📁 Project Structure

```
Cysic Testnet/
├── cysic_launcher/
│   ├── main.py              Entry point — Rich CLI menu and all features
│   └── config/
│       └── settings.json    Node settings (auto-created on first run)
├── about/
│   └── about.md             Cysic network description and hashtags
├── requirements.txt         Python dependencies (rich)
├── run.bat                  Windows one-click launcher
└── README.md                This file
```

---

## ❓ FAQ

<details>
<summary><b>ModuleNotFoundError: No module named 'rich'</b></summary>

Run option **1** from the menu, use `run.bat` (auto-installs), or manually:
```bash
pip install -r requirements.txt
```
</details>

<details>
<summary><b>What is Cysic Network?</b></summary>

Cysic is a full-stack compute infrastructure for verifiable AI, ZK proofs, and decentralized compute. It uses Proof-of-Compute consensus (based on useful computational work, not capital). The network features prover nodes, verifier nodes, hardware acceleration via custom ASIC chips, and a dual-token model ($CYS + $CGT).
</details>

<details>
<summary><b>What is ComputeFi?</b></summary>

ComputeFi is Cysic's framework that transforms compute into a verifiable, financialized resource. It supports ZK proof generation, AI inference, and mining workloads through a decentralized marketplace. Compute contributors earn rewards through Digital Compute Cube NFTs and token incentives.
</details>

<details>
<summary><b>Full node vs Validator — which should I choose?</b></summary>

**Full node** syncs and validates the chain — lower resource requirements, good for monitoring.
**Validator** actively participates in block production — requires staking and higher uptime. Start with `full` during testnet, upgrade to `validator` when ready.
</details>

<details>
<summary><b>Where is the settings file stored?</b></summary>

Settings are saved at `cysic_launcher/config/settings.json`. The directory and file are auto-created on first launch. You can edit the JSON directly or use the Settings menu (option 2).
</details>

<details>
<summary><b>Can I run this on a VPS?</b></summary>

Yes. The launcher works on any system with Python 3.8+. On Linux VPS:
```bash
screen -S cysic
python cysic_launcher/main.py
# Press Ctrl+A, D to detach
```
</details>

---

## ⚠️ Disclaimer

This tool is for **educational and testnet purposes only**. The authors are not affiliated with Cysic Network. This is a terminal launcher / configuration helper — not a full node implementation. Refer to the [official Cysic documentation](https://docs.cysic.xyz) for node operation. The authors are not responsible for any issues arising from node misconfiguration.

---

<div align="center">

If this launcher helped you set up a Cysic node, consider leaving a ⭐

</div>
