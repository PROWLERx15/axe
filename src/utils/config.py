import os
from dotenv import load_dotenv
from web3 import Web3


load_dotenv()
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

CHAIN_CONFIG = {
    "ethereum": {"chain_id": 1, "rpc_url": os.getenv("ETHEREUM_RPC_URL")},
    "eth-sepolia": {"chain_id": 11155111, "rpc_url": os.getenv("ETH_SEPOLIA_RPC_URL")},

    "op-mainnet": {"chain_id": 42161, "rpc_url": os.getenv("OP_MAINNET_RPC_URL")},
    "op-sepolia": {"chain_id": 42161, "rpc_url": ("OP_SEPOLIA_RPC_URL")},

    "arbitrum": {"chain_id": 42161, "rpc_url": os.getenv("ARBITRUM_RPC_URL")},
    "arb-sepolia": {"chain_id": 421614, "rpc_url": os.getenv("ARB_SEPOLIA_RPC_URL")},

    "base": {"chain_id": 8453, "rpc_url": os.getenv("BASE_RPC_URL")},
    "base-sepolia": {"chain_id": 84532, "rpc_url": os.getenv("BASE_SEPOLIA_RPC_URL")},

    "avalanche": {"chain_id": 43114, "rpc_url": os.getenv("AVALANCHE_RPC_URL")},
    "avalanche-fuji": {"chain_id": 43113, "rpc_url": os.getenv("AVALANCHE_FUJI_RPC_URL")},

    "polygon": {"chain_id": 137, "rpc_url": os.getenv("POLYGON_RPC_URL")},
    "polygon-amoy": {"chain_id": 80002, "rpc_url": os.getenv("POLYGON_AMOY_RPC_URL")}
}


def get_web3(chain: str) -> Web3:
    chain = chain.lower()
    if chain not in CHAIN_CONFIG:
        raise ValueError(f"Unsupported Chain: {chain}")
    else:
        web3 = Web3(Web3.HTTPProvider(
            f"{CHAIN_CONFIG[chain.lower()]['rpc_url']}"))
        return web3
