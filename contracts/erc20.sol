// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract erc20hw {

    string public constant name = "erc20hw";
    string public constant symbol = "kekCoin";
    uint8 public constant decimals = 8;  

    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    event Approval(address indexed _owner, address indexed _spender, uint256 _value);

    mapping(address => uint256) _balances;

    mapping(address => mapping (address => uint256)) _allowance;
    
    uint256 _totalSupply;

    constructor(uint256 total) {  
        _totalSupply = total;
        _balances[msg.sender] = _totalSupply;
    }  

    function totalSupply() public view returns (uint256) {
	    return _totalSupply;
    }
    
    function balanceOf(address _owner) public view returns (uint256 balance) {
        return _balances[_owner];
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_value <= _balances[msg.sender]);
        require(_balances[_to] + _value >= _balances[_to]);

        _balances[msg.sender] = _balances[msg.sender] - _value;
        _balances[_to] = _balances[_to] + _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_value <= _balances[msg.sender]);

        _allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function allowance(address _owner, address _spender) public view returns (uint256 remaining) {
        return _allowance[_owner][_spender];
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_value <= _balances[_from]);    
        require(_value <= _allowance[_from][msg.sender]);
        require(_balances[_to] + _value >= _balances[_to]);
    
        _balances[_from] = _balances[_from] - _value;
        _allowance[_from][msg.sender] = _allowance[_from][msg.sender] - _value;
        _balances[_to] = _balances[_to] + _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    function createTokens(uint256 _value) public returns (bool success) {
        require(_totalSupply + _value >= _totalSupply);

        _totalSupply = _totalSupply + _value;
        _balances[msg.sender] = _balances[msg.sender] + _totalSupply;
        return true;
    }
}
