*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kaisa
    Set Password  kaisa123
    Set Password Confirmation  kaisa123
    Submit Username And Password
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kaisa123
    Set Password Confirmation  kaisa123
    Submit Username And Password
    Register Should Fail With Message  Username must contain at least 3 characters a-z

Register With Valid Username And Too Short Password
    Set Username  kaisb
    Set Password  kaisa12
    Set Password Confirmation  kaisa12
    Submit Username And Password
    Register Should Fail With Message  Password must contain at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  kaisc
    Set Password  kaisa123
    Set Password Confirmation  kaisa12
    Submit Username And Password
    Register Should Fail With Message  Password and password confirmation don't match


*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Username And Password
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}
