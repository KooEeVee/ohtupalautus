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

Login After Successful Registration
    Create User And Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ka
    Set Password  kaisa123
    Set Password Confirmation  kaisa123
    Submit Username And Password
    Register Should Fail With Message  Username must contain at least 3 characters a-z
    Click Login Link
    Set Username  ka
    Set Password  kaisa123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

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

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open

Submit Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Click Login Link
    Click Link  Login
    Login Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
