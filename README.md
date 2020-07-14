# Expense Tracker with Python GUI..

## Requirements 

You need to install the following modules in order to run the code without errors using the command `pip install {module_name}`  : os, pickle, tkintertable, matplotlib, datetime, cryptography.

Expense Tracker helps you with track your expenses which is made with a tkinter GUI.

### Three Files

In the file exp_track.py you can create multiple accounts by using the button create account, but in simple_track.py you can only use one account for which you should change the username and password by yourself in the code itself. And the last one which is the secure one which saves the encrypted data and decrypts it when it is displayed to the user. Not only expenses but also all the credentials are encrypted.

### Secure Expenses Tracker

In the file secure_exp_track.py the data is saved after encryption with an unique key for every expense and every user credentials which increases the security of the program. The keys are generated randomly for every piece of data. While displaying the data it will be decrypted and then decode into utf-8 format.

#### Create Account and Login

You should create acount at first and then you are automatically logged in. You can again logout and create another account or login again. Your data won't be lost but instead saved as a .txt file which will be loaded when you login again..

#### Add an Expense

You can Add an Expense by clicking on the button `Add an Expense` and there you can add it's Name and Amount....  But.. It will also record the current date and time which is the time you added the record.

#### List all Expenses

It lists all your Expenses with the total amount at the end.

#### Show the Graph

It shows the graph of your total expenses by date. With this option you can See the graph and compare your expenses on the daily basis..
