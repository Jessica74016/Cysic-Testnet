# Cysic Testnet Node Manager

Management tool for running **Cysic** ZK proof verification/generation nodes on the testnet.

## Features

- **Node setup** — initialize data directory and download binaries
- **Verifier mode** — verify zero-knowledge proofs and earn rewards
- **Prover mode** — generate ZK proofs for the network
- **Status monitoring** — real-time node metrics and proof counts
- **Configuration management** — interactive setup with persistent config
- **Auto-update** — keep node binaries up to date

## Requirements

- Python 3.9+
- Cysic node binaries (download from https://cysic.xyz)

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Run the interactive setup:

```bash
python main.py
# Select "Configure node" from the menu
```

Or edit `config/settings.json` directly:

```json
{
  "node_type": "verifier",
  "rpc_endpoint": "https://rpc-testnet.cysic.xyz",
  "reward_address": "0x...",
  "max_proofs_parallel": 4
}
```

## Usage

```bash
python main.py
```

## License

MIT
