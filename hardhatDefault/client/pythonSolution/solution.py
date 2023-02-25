from web3 import Web3
import web3

w3 = Web3(Web3.WebsocketProvider('wss://goerli.infura.io/ws/v3/d58ad49ac6be44d781b614ada33a811b'))

address = Web3.toChecksumAddress('0x74E2Fa41f96550f070E51AE596E01157a9eF548E')

contract = w3.eth.contract(
	address=address,
	abi=[
    {
        "anonymous": "false",
        "inputs": [
            {
                "indexed": "true",
                "internalType": "address",
                "name": "_caller",
                "type": "address"
            },
            {
                "indexed": "true",
                "internalType": "address",
                "name": "_index",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "val",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bool",
                        "name": "flag",
                        "type": "bool"
                    },
                    {
                        "internalType": "string",
                        "name": "field1",
                        "type": "string"
                    },
                    {
                        "internalType": "int256",
                        "name": "field2",
                        "type": "int256"
                    }
                ],
                "indexed": "false",
                "internalType": "struct mapper.elem",
                "name": "_value",
                "type": "tuple"
            }
        ],
        "name": "Add",
        "type": "event"
    },
    {
        "anonymous": "false",
        "inputs": [
            {
                "indexed": "true",
                "internalType": "address",
                "name": "_caller",
                "type": "address"
            },
            {
                "indexed": "true",
                "internalType": "address",
                "name": "_index",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "val",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bool",
                        "name": "flag",
                        "type": "bool"
                    },
                    {
                        "internalType": "string",
                        "name": "field1",
                        "type": "string"
                    },
                    {
                        "internalType": "int256",
                        "name": "field2",
                        "type": "int256"
                    }
                ],
                "indexed": "false",
                "internalType": "struct mapper.elem",
                "name": "_value",
                "type": "tuple"
            }
        ],
        "name": "Delete",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_addr",
                "type": "address"
            }
        ],
        "name": "remove",
        "outputs": [
            {
                "internalType": "bool",
                "name": "success",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_addr",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_val",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "_flag",
                "type": "bool"
            },
            {
                "internalType": "string",
                "name": "_firstfield",
                "type": "string"
            },
            {
                "internalType": "int256",
                "name": "_secondfield",
                "type": "int256"
            }
        ],
        "name": "set",
        "outputs": [
            {
                "internalType": "bool",
                "name": "success",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_addr",
                "type": "address"
            }
        ],
        "name": "get",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "val",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bool",
                        "name": "flag",
                        "type": "bool"
                    },
                    {
                        "internalType": "string",
                        "name": "field1",
                        "type": "string"
                    },
                    {
                        "internalType": "int256",
                        "name": "field2",
                        "type": "int256"
                    }
                ],
                "internalType": "struct mapper.elem",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]);

print("Get result for set element: ", contract.functions.get('0xA338250363a8C267a06a4CaE482f7D0731E830Bd').call())
print("Get result for unset element: ", contract.functions.get('0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f').call())


def getAddEventsByAdress(callerAdress, contract):
	transferEvents = contract.events.Add.createFilter(fromBlock=0, address="0x74E2Fa41f96550f070E51AE596E01157a9eF548E")
	transferEvents.get_all_entries()

print(getAddEventsByAdress('0xA338250363a8C267a06a4CaE482f7D0731E830Bd', contract))
