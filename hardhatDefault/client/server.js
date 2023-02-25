const Web3 = require("web3");
const ethNetwork = 'https://goerli.infura.io/v3/d58ad49ac6be44d781b614ada33a811b';
const web3 = new Web3(new Web3.providers.HttpProvider(ethNetwork));

//copied from Remix IDE
let contract = new web3.eth.Contract([
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "_caller",
                "type": "address"
            },
            {
                "indexed": true,
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
                "indexed": false,
                "internalType": "struct mapper.elem",
                "name": "_value",
                "type": "tuple"
            }
        ],
        "name": "Add",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "_caller",
                "type": "address"
            },
            {
                "indexed": true,
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
                "indexed": false,
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
], '0x74E2Fa41f96550f070E51AE596E01157a9eF548E');

contract.methods.get('0xA338250363a8C267a06a4CaE482f7D0731E830Bd').call().then(console.log);

contract.getPastEvents('AllEvents', 
    {
        fromBlock: 0,
        toBlock: 'latest'
    },
    async (err, events) => { console.log(events)}
    );

web3.eth.getBalance('0x74E2Fa41f96550f070E51AE596E01157a9eF548E', async (err, result) => {
    if (err) {
        console.log(err);
        return;
    }
    let balance = web3.utils.fromWei(result, "ether");
    console.log(balance + " ETH");
});
