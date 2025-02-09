// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TokenDistribution {

    string public name = "GLDTR Token Distribution";
    address public owner;
    uint256 public totalSupply = 1000000000 * 10**18; // 1 billion tokens
    uint256 public tokensDistributed;

    mapping(address => uint256) public balanceOf;

    event TokensDistributed(address indexed to, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
        balanceOf[owner] = totalSupply;
    }

    function distributeTokens(address recipient, uint256 amount) public onlyOwner {
        require(balanceOf[owner] >= amount, "Insufficient tokens for distribution");
        balanceOf[owner] -= amount;
        balanceOf[recipient] += amount;
        tokensDistributed += amount;

        emit TokensDistributed(recipient, amount);
    }

    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "Invalid address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    function getDistributionStatus() public view returns (uint256 remainingTokens, uint256 distributedTokens) {
        return (balanceOf[owner], tokensDistributed);
    }
}
