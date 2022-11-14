*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Input Credentials

*** Test Cases ***
Register With Valid Username And Password
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kaisa  kaisa123
    Output Should Contain  User with username kaisa already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ka  kaisa123
    Output Should Contain  Username must contain at least 3 characters a-z

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  kaisb  kaisa
    Output Should Contain  Password must contain at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  kaisb  kaisakai
    Output Should Contain  Password must contain other characters than letters a-z

*** Keywords ***
Input New Command And Input Credentials
    Input New Command
    Input Credentials  kaisa  kaisa123