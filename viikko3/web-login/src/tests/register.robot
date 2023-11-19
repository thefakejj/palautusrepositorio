*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  balle
    Set Password  balle123
    Set Password confirmation  balle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  b
    Set Password  balle123
    Set Password confirmation  balle123
    Submit Credentials
    Register Should Fail With Message  Username shorter than 3

Register With Valid Username And Invalid Password
    Set Username  baller
    Set Password  ballermoves
    Set Password confirmation  ballermoves
    Submit Credentials
    Register Should Fail With Message  Password consists of only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  baller
    Set Password  ballermoves123
    Set Password confirmation  ballermoves12
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation must match


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}

Submit Credentials
    Click Button  Register

# *** Keywords ***
# Login Should Succeed
#     Main Page Should Be Open

# Login Should Fail With Message
#     [Arguments]  ${message}
#     Login Page Should Be Open
#     Page Should Contain  ${message}

# Create User And Go To Login Page
#     Create User  kalle  kalle123
#     Go To Login Page
#     Login Page Should Be Open
# *** Test Cases ***
# Login With Correct Credentials
#     Set Username  kalle
#     Set Password  kalle123
#     Submit Credentials
#     Login Should Succeed

# Login With Incorrect Password
#     Set Username  kalle
#     Set Password  kalle456
#     Submit Credentials
#     Login Should Fail With Message  Invalid username or password