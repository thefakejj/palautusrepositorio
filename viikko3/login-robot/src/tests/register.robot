*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command


*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  balle  balle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  kalle123
    Output Should Contain  Username shorter than 3

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ääää  kalle123
    Output Should Contain  Username contains invalid characters

Register With Valid Username And Too Short Password
    Input Credentials  balle  balle12
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  balle  BALLEBALLE
    Output Should Contain  Password consists of only letters