# Create Lots of MI accounts!!!

## Requirement
- python3
- ```pip install selenium```
- Firefox browser
- geckodriver(a web driver for Firefox)
    - [Dowload from Github, Click here](https://github.com/mozilla/geckodriver/releases)

## How to use
- open auto.py, edit 'main_account' and 'password'
- move geckodriver file (eg.geckodriver.exe) into this directory so that auto.py can use it
- ```$ python auto.py```
- Magic is about to happen!


# Get Web Cookie From Many Account(取得帳號海的cookie)
## Notice!
- This solution is for the situation that many accounts use the same password.
## How to use
- First, edit 'account_list.txt' file. Write your accounts (without email suffix) into the file, one line for one account.
- Edit the password and email suffix in 'get_cookie.py'
-  ```$ python get_cookis.py```
- Or, you can use a file to catch the output from the terminal:
- ```$ python get_cookis.py > output.txt```