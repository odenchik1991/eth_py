
from web3 import Web3

# Connect to Ethereum network (Infura URL for Mainnet, replace with your endpoint)
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection is successful
if web3.isConnected():
    print("Successfully connected to Ethereum network!")
else:
    print("Failed to connect.")
    exit()

# Input Ethereum wallet address
wallet_address = input("Enter an Ethereum wallet address: ")

# Validate the address
if not web3.isAddress(wallet_address):
    print("Invalid Ethereum address!")
else:
    # Fetch and convert balance to Ether
    balance_wei = web3.eth.get_balance(wallet_address)
    balance_eth = web3.fromWei(balance_wei, 'ether')
    print(f"Wallet Balance: {balance_eth} ETH")
