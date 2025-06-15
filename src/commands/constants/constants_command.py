import typer
from rich.table import Table
from rich.console import Console
from rich.panel import Panel

constants_app = typer.Typer(
    help="Frequently used EVM constants at your fingertips - addresses, gas costs, uint limits, and more.")

console = Console()

UINT_MAX = {
    "uint8":  {"dec": str(2**8 - 1), "hex": hex(2**8 - 1)},
    "uint16": {"dec": str(2**16 - 1), "hex": hex(2**16 - 1)},
    "uint24": {"dec": str(2**24 - 1), "hex": hex(2**24 - 1)},
    "uint32": {"dec": str(2**32 - 1), "hex": hex(2**32 - 1)},
    "uint40": {"dec": str(2**40 - 1), "hex": hex(2**40 - 1)},
    "uint48": {"dec": str(2**48 - 1), "hex": hex(2**48 - 1)},
    "uint64": {"dec": str(2**64 - 1), "hex": hex(2**64 - 1)},
    "uint96": {"dec": str(2**96 - 1), "hex": hex(2**96 - 1)},
    "uint160": {"dec": str(2**160 - 1), "hex": hex(2**160 - 1)},
    "uint256": {"dec": str(2**256 - 1), "hex": hex(2**256 - 1)},
}

ADDRESS = {
    "Zero Address": {
        "address": "0x0000000000000000000000000000000000000000",
        "description": "Default zero address"
    },
    "Burn Address": {
        "address": "0x000000000000000000000000000000000000dEaD",
        "description": "Used to burn tokens permanently"
    },
    "ecrecover (0x01)": {
        "address": "0x0000000000000000000000000000000000000001",
        "description": "Elliptic curve digital signature recovery"
    },
    "sha256 (0x02)": {
        "address": "0x0000000000000000000000000000000000000002",
        "description": "SHA-256 hash function"
    },
    "ripemd160 (0x03)": {
        "address": "0x0000000000000000000000000000000000000003",
        "description": "RIPEMD-160 hash function"
    },
    "identity (0x04)": {
        "address": "0x0000000000000000000000000000000000000004",
        "description": "Returns input unmodified"
    },
    "modexp (0x05)": {
        "address": "0x0000000000000000000000000000000000000005",
        "description": "Modular exponentiation (big integers)"
    },
    "bn128Add (0x06)": {
        "address": "0x0000000000000000000000000000000000000006",
        "description": "Addition on alt_bn128 elliptic curve"
    },
    "bn128Mul (0x07)": {
        "address": "0x0000000000000000000000000000000000000007",
        "description": "Multiplication on alt_bn128 elliptic curve"
    },
    "bn128Pairing (0x08)": {
        "address": "0x0000000000000000000000000000000000000008",
        "description": "Pairing check on alt_bn128 curve"
    },
    "blake2f (0x09)": {
        "address": "0x0000000000000000000000000000000000000009",
        "description": "BLAKE2b compression function"
    }
}


BYTES = {
    "bytes1": {"zero": "0x00", "max": "0xff"},
    "bytes4": {"zero": "0x" + "00" * 4, "max": "0xffffffff"},
    "bytes20": {"zero": "0x" + "00" * 20, "max": "0x" + "ff" * 20},
    "bytes32": {"zero": "0x" + "00" * 32, "max": "0x" + "ff" * 32},
}

ETH_UNITS = {
    "wei":    {"wei": f"{1} (1e0)",        "eth": "0.000000000000000001"},
    "gwei":   {"wei": f"{10**9} (1e9)",    "eth": "0.000000001"},
    "szabo":  {"wei": f"{10**12} (1e12)",  "eth": "0.000001"},
    "finney": {"wei": f"{10**15} (1e15)",  "eth": "0.001"},
    "ether":  {"wei": f"{10**18} (1e18)",  "eth": "1"},
}

CHAIN_IDS = {
    "Ethereum Mainnet": "1",
    "Sepolia Testnet": "11155111",
    "Holesky Testnet": "17000",
    "Polygon Mainnet": "137",
    "Polygon Amoy Testnet": "80002",
    "Polygon zkEVM": "1101",
    "Polygon zkEVM Testnet": "1442",
    "BNB Smart Chain Mainnet": "56",
    "BNB Smart Chain Testnet": "97",
    "Arbitrum One": "42161",
    "Arbitrum Nova": "42170",
    "Arbitrum Sepolia": "421614",
    "Optimism": "10",
    "Optimism Sepolia": "11155420",
    "Base": "8453",
    "Base Sepolia": "84532",
    "Avalanche C-Chain": "43114",
    "Avalanche Fuji Testnet": "43113",
    "Fantom Opera": "250",
    "Fantom Testnet": "4002",
    "Cronos Mainnet": "25",
    "Cronos Testnet": "338",
    "Gnosis": "100",
    "Gnosis Chiado Testnet": "10200",
    "Moonbeam": "1284",
    "Moonriver": "1285",
    "Moonbase Alpha": "1287",
    "Celo Mainnet": "42220",
    "Celo Alfajores Testnet": "44787",
    "Aurora Mainnet": "1313161554",
    "Aurora Testnet": "1313161555",
    "Harmony Mainnet Shard 0": "1666600000",
    "Linea": "59144",
    "Linea Goerli": "59140",
    "Mantle": "5000",
    "Mantle Testnet": "5001",
    "Scroll": "534352",
    "Scroll Sepolia": "534351",
    "zkSync Era": "324",
    "zkSync Era Sepolia": "300",
    "Blast": "81457",
    "Blast Sepolia": "168587773",
    "Mode": "34443",
    "Fraxtal": "252",
    "Metis Andromeda": "1088",
    "Kava EVM": "2222",
    "Hardhat Local": "31337",
    "Ganache Local": "1337",
    "Anvil Local": "31337"
}


GAS_CONSTANTS = {
    "Transaction Costs": [
        {
            "name": "TX_BASE_GAS",
            "value": "21000",
            "description": "Base gas cost for a standard ETH transfer"
        }
    ],
    "Calldata": [
        {
            "name": "GAS_PER_ZERO_BYTE",
            "value": "4",
            "description": "Gas per zero byte in calldata"
        },
        {
            "name": "GAS_PER_NON_ZERO_BYTE",
            "value": "16",
            "description": "Gas per non-zero byte in calldata"
        }
    ],
    "Account Access": [
        {
            "name": "ACCESS_LIST_ADDRESS",
            "value": "2400",
            "description": "Gas for an address in the access list"
        },
        {
            "name": "ACCESS_LIST_STORAGE_KEY",
            "value": "1900",
            "description": "Gas for a storage key in the access list"
        }
    ],
    "Storage": [
        {
            "name": "SLOAD_COLD_GAS",
            "value": "2100",
            "description": "Gas cost for reading a cold storage slot"
        },
        {
            "name": "SLOAD_WARM_GAS",
            "value": "100",
            "description": "Gas cost for reading a warm storage slot"
        },
        {
            "name": "SSTORE_SET_COLD_GAS",
            "value": "22100",
            "description": "Setting storage from zero (cold access)"
        },
        {
            "name": "SSTORE_RESET_COLD_GAS",
            "value": "5000",
            "description": "Resetting storage to non-zero (cold access)"
        },
        {
            "name": "SSTORE_CLEAR_REFUND",
            "value": "4800",
            "description": "Refund for clearing storage to zero"
        }
    ],
    "Call Operations": [
        {
            "name": "CALL_COLD_ACCOUNT_ACCESS",
            "value": "2600",
            "description": "Extra gas for calling a cold account"
        },
        {
            "name": "CALL_WARM_STORAGE_READ",
            "value": "100",
            "description": "Gas for calling a warm account"
        }
    ],
    "Contract Creation": [
        {
            "name": "NEW_CONTRACT_CREATION",
            "value": "32000",
            "description": "Gas for creating a new smart contract"
        },
        {
            "name": "INITCODE_WORD",
            "value": "2",
            "description": "Gas per word in initcode"
        }
    ],
    "Logging": [
        {
            "name": "LOG_TOPIC_GAS",
            "value": "375",
            "description": "Gas per topic in a LOG"
        },
        {
            "name": "LOG_DATA_GAS",
            "value": "8",
            "description": "Gas per byte of data in a LOG"
        }
    ],
    "Memory": [
        {
            "name": "MEMORY_EXPANSION_LINEAR",
            "value": "3",
            "description": "Linear gas cost for memory expansion"
        },
        {
            "name": "MEMORY_EXPANSION_QUADRATIC_DIVISOR",
            "value": "512",
            "description": "Quadratic cost divisor for memory expansion"
        }
    ],
    "Opcodes": [
        {"name": "JUMPDEST_GAS", "value": "1",
            "description": "Gas for JUMPDEST opcode"},
        {"name": "PUSH_GAS", "value": "3", "description": "Gas for PUSH opcode"},
        {"name": "DUP_GAS", "value": "3", "description": "Gas for DUP opcode"},
        {"name": "SWAP_GAS", "value": "3", "description": "Gas for SWAP opcode"},
        {"name": "ADD_GAS", "value": "3", "description": "Gas for ADD opcode"},
        {"name": "MUL_GAS", "value": "5", "description": "Gas for MUL opcode"},
        {"name": "SUB_GAS", "value": "3", "description": "Gas for SUB opcode"},
        {"name": "DIV_GAS", "value": "5", "description": "Gas for DIV opcode"},
        {"name": "SDIV_GAS", "value": "5", "description": "Gas for SDIV opcode"},
        {"name": "EXP_GAS", "value": "10", "description": "Base gas for EXP opcode"},
        {"name": "EXP_BYTE_GAS", "value": "50",
            "description": "Gas per byte of exponent in EXP"},
        {"name": "SHA3", "value": "30", "description": "Base gas cost for SHA3 opcode"},
        {"name": "SHA3_WORD", "value": "6",
            "description": "Gas per word hashed with SHA3"}
    ],
    "Block/Tx Info": [
        {"name": "BLOCKHASH_GAS", "value": "20",
            "description": "Gas for BLOCKHASH opcode"},
        {"name": "BALANCE_GAS", "value": "700",
            "description": "Gas for BALANCE opcode"},
        {"name": "EXTCODEHASH_GAS", "value": "700",
            "description": "Gas for EXTCODEHASH opcode"},
        {"name": "EXTCODESIZE_GAS", "value": "700",
            "description": "Gas for EXTCODESIZE opcode"},
        {"name": "EXTCODECOPY_GAS", "value": "700",
            "description": "Gas for EXTCODECOPY opcode"}
    ],
    "Selfdestruct": [
        {
            "name": "SELFDESTRUCT_GAS",
            "value": "5000",
            "description": "Gas for SELFDESTRUCT"
        }
    ],
    "Precompiled Contracts": [
        {"name": "ECRECOVER_GAS", "value": "3000",
            "description": "Gas cost for ecrecover precompile"},
        {"name": "SHA256_GAS", "value": "60",
            "description": "Base gas for SHA256 precompile"},
        {"name": "SHA256_WORD", "value": "12",
            "description": "Gas per word for SHA256 precompile"},
        {"name": "RIPEMD160_GAS", "value": "600",
            "description": "Base gas for RIPEMD160 precompile"},
        {"name": "RIPEMD160_WORD", "value": "120",
            "description": "Gas per word for RIPEMD160 precompile"},
        {"name": "IDENTITY_GAS", "value": "15",
            "description": "Base gas for IDENTITY precompile"},
        {"name": "IDENTITY_WORD", "value": "3",
            "description": "Gas per word for IDENTITY precompile"}
    ]
}


@constants_app.command("uint", help="Max decimal and hex values of common uint types")
def uint_constants():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("UINT", style="cyan")
    table.add_column("Decimal (Max Value)", overflow="fold")
    table.add_column("Hex (Max Value)", overflow="fold")

    for uint, value in UINT_MAX.items():
        table.add_row(uint, value['dec'], value['hex'])

    console.print(table)


@constants_app.command("address", help="Standard Ethereum addresses: zero, burn, and precompiles")
def address_constants():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="cyan")
    table.add_column("Address (Ethereum)", overflow="fold")
    table.add_column("Description", overflow="fold")

    for address, details in ADDRESS.items():
        table.add_row(address, details['address'], details['description'])

    console.print(table)


@constants_app.command("bytes", help="Zero and Max values for common fixed-sized byte types")
def bytes_constants():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Bytes", style="cyan")
    table.add_column("Zero Value", overflow="fold")
    table.add_column("Max Value", overflow="fold")

    for bytes_type, value in BYTES.items():
        table.add_row(bytes_type, value['zero'], value['max'])

    console.print(table)


@constants_app.command("eth-units", help="ETH units and their equivalent values in Wei and Ether")
def eth_unit_constants():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Unit", style="cyan")
    table.add_column("Value in Wei", overflow="fold")
    table.add_column("Value in ETH", overflow="fold")

    for eth_units, value in ETH_UNITS.items():
        table.add_row(eth_units, value['wei'], value['eth'])

    console.print(table)


@constants_app.command("chainid", help="Chain IDs of major EVM chains")
def chainid_constants():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="cyan")
    table.add_column("Chainid", overflow="fold")

    for name, chain_id in CHAIN_IDS.items():
        table.add_row(name, chain_id)

    console.print(table)


@constants_app.command("gas", help="Gas costs for EVM opcodes, transactions, calldata, and storage operations")
def gas_constants():
    for category, entries in GAS_CONSTANTS.items():
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Operation", style="cyan")
        table.add_column("Cost (Gas Units)", overflow="fold")
        table.add_column("Description", overflow="fold")

        for entry in entries:
            table.add_row(entry['name'], entry['value'], entry['description'])

        console.rule(f"[bold blue]{category}[/bold blue]")
        console.print(table)


@constants_app.command("all", help="All EVM related constants in one view")
def all_constants():
    console.rule("[bold green]UINT Constants[/bold green]")
    uint_constants()

    console.rule("[bold green]ADDRESS Constants[/bold green]")
    address_constants()

    console.rule("[bold green]BYTES Constants[/bold green]")
    bytes_constants()

    console.rule("[bold green]ETH Units[/bold green]")
    eth_unit_constants()

    console.rule("[bold green]Chain IDs[/bold green]")
    chainid_constants()

    console.rule("[bold green]Gas Constants[/bold green]")
    gas_constants()
