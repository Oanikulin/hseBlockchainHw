// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract mapper {

    struct elem {
        uint val;
        bool flag; 
        string field1;
        int field2;
    } 

    event Add(address indexed _caller, address indexed _index, elem _value);
    event Delete(address indexed _caller, address indexed _index, elem _value);

    mapping(address => elem) _mapping;

    function get(address _addr) public view returns (elem memory) {
        // If the value was never set, it will return the default value.
        return _mapping[_addr];
    }

    function set(address _addr, uint _val, bool _flag, string calldata _firstfield, int _secondfield) public returns (bool success) {
        // Update the value at this address

        _mapping[_addr] = elem(_val, _flag, _firstfield, _secondfield);
        emit Add(msg.sender, _addr, _mapping[_addr]);
        return true;
    }

    function remove(address _addr) public returns (bool success) {
        // Reset the value to the default value.
        emit Delete(msg.sender, _addr, _mapping[_addr]);
        delete _mapping[_addr];
        return true;
    }
}