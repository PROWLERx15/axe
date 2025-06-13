import requests
import json
from src.utils.config import ETHERSCAN_API_KEY, CHAIN_CONFIG, get_web3


def decode_using_transaction_hash(tx_hash: str, chain: str):
    chain = chain.lower()
    web3 = get_web3(chain)

    try:
        tx = web3.eth.get_transaction(tx_hash)
    except Exception as e:
        raise RuntimeError(f"Error fetching transaction!  \n{e}")

    abi_endpoint = f"https://api.etherscan.io/v2/api?chainid={CHAIN_CONFIG[chain]['chain_id']}&module=contract&action=getabi&address={tx['to']}&apikey={ETHERSCAN_API_KEY}"

    try:
        response = requests.get(abi_endpoint)
        response_data = response.json()
    except Exception as e:
        raise RuntimeError(f"Error fetching ABI! \n{e}")
    
    if response_data['status'] != '1' or not response_data['result']:
        raise RuntimeError(f"ABI Messsage: {response_data['message']} \nABI Result: {response_data['result']}")


    if isinstance(response_data['result'], str):                                                                                               
        abi = json.loads(response_data['result'])
    else:
        abi = response_data['result']
    
    try:
        contract = web3.eth.contract(address=tx['to'], abi=abi)
        func_obj, func_params = contract.decode_function_input(tx['input'])
        return (func_obj, func_params)
    except Exception as e:
        raise RuntimeError(f"Error decoding Calldata! \n{e}")


def decode_using_abi(calldata: str, abi: list, chain: str):
    chain = chain.lower()

    try:
        web3 = get_web3(chain)
        contract = web3.eth.contract(abi=abi)
        func_obj, func_params = contract.decode_function_input(calldata)
        return (func_obj, func_params)
    except Exception as e:
        raise RuntimeError(f"Error decoding Calldata! \n{e}")


def decode_using_address(calldata: str, address: str, chain: str):
    chain = chain.lower()

    abi_endpoint = f"https://api.etherscan.io/v2/api?chainid={CHAIN_CONFIG[chain]['chain_id']}&module=contract&action=getabi&address={address}&apikey={ETHERSCAN_API_KEY}"

    try:
        response = requests.get(abi_endpoint)
        response_data = response.json()
        
    except Exception as e:
        raise RuntimeError(f"Error decoding Calldata! \n{e}")
    
    if response_data['status'] != '1' or not response_data['result']:
        raise RuntimeError(f"ABI Messsage: {response_data['message']} \nABI Result: {response_data['result']}")
    
    if isinstance(response_data['result'], str):                                                                                               
        abi = json.loads(response_data['result'])
    else:
        abi = response_data['result']

    try:
        web3 = get_web3(chain)
        contract = web3.eth.contract(address=address, abi=abi)
        func_obj, func_params = contract.decode_function_input(calldata)
        return (func_obj, func_params)
    except Exception as e:
        raise RuntimeError(f"Error Decoding Calldata! \n{e}")
