// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract UIDCheck{
    address public owner;
    mapping( string => bool ) public uidMap;

    modifier onlyOwner(){
        require(msg.sender == owner, "not allowed");
        _;
    }

    constructor() {
        owner = msg.sender;
        uidMap["26dd8b88024778710c3052a634cf1d26dffa5d33d8d19278bb479fe22e52f8a7"] = true;

    }
    function checkUid(string memory _uid) public view{
        require(uidMap[_uid], "Given UID is not in the whitelist.");
    }

    function insertUid(string memory _uid) public onlyOwner{
        uidMap[_uid] = true;
    }
    function removeUid(string memory _uid) public onlyOwner{
        uidMap[_uid] = false;
    }

}