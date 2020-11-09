# Mnemonic Assignment

### Functionality

The application is a basic REST API for performing transactions between two bank accounts. At the landing page you get to choose between pre-initiatied accounts as the source account, then you choose the destination account form the remaining set of accounts (excluding the source) and then finally you insert the amount you want to transfer. If there is enough money on the source account the transaction will result in a "OK 200" message and the money is transferred, otherwise you get an error message and the money remains in place. Under "See Transaction History" you can see an overview of all historical transactions.


### Local version  
Instructions for running the application local.

##### Prerequisites 
If you already have Git, pip and Python installed, you can skip directly to 'Installation'

1. To install Python, type in your terminal
    `sudo apt-get install python3`
2. If you are on a macOS install Git by typing the following command. If you don't have Git installed, this will prompt you to install it.  
    `git --version`  
If your are on a Linux and on Fedora you can use the following command:  
 `sudo dnf install git-all`  
And if you are on a Linux and on Debian-based distribution use:  
 `sudo apt install git-all`  
3. Finally, install pip with this command
    `sudo easy_install pip`

#### Installation
If you want to run it at once, type the following in your terminal:
```
git clone https://github.com/sjurwold1997/mnemonic_assignment.git && cd mnemonic_assignment && virtualenv venv && source venv/bin/activate && pip install -r requirements.txt && python manage.py migrate && python manage.py runserver
```

Underneath is a step-by-step guide with the same functionality as the snippet above.

Follow these steps to run the application on your local machine:
1. Clone our git repo in terminal  
```
git clone https://github.com/sjurwold1997/mnemonic_assignment.git
```
2. Go to the directory bank by typing   
`cd mnemonic_assignment`
3. Create a virtual environment.  
   `virtualenv env`
4. Activate the virtual environment by typing   
    . env/bin/activate` 
    You should now see (venv) in your command line, indicating venv is active.
5.  After successfully cloning, you need to install all the required packages. Run the following command in Terminal:  
    `pip install -r requirements.txt`
6. Get the database up to date  
     `python manage.py migrate`
7. Run the following command  
    `python manage.py runserver`. 
8. Go to 127.0.0.1:8000 or localhost:8000 to run the app in a browser

By entering "localhost:8000" you will land in a page with a default database.

    
### Tests
I have written some basic tests for the functionality of the program.

If you want to run the tests you can use the following command in the terminal. Make sure you are inside the folder gruppe-33:  
    `python manage.py test`


