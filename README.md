# Mnemonic Assignment


### Local version  
Instructions for running the applications local.

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
Follow these steps to run the application on your local machine:
1. Clone our git repo in terminal  
```
git clone https://github.com/sjurwold1997/mnemonic_assignment.git
```
2. Go to the directory bank by typing   
`cd bank`
3. Create a virtual environment.  
   `virtualenv env`
4. Activate the virtual environment by typing   
    . env/bin/activate` 
    You should now see (venv) in your command line, indicating venv is active.
5.  After successfully cloning, you need to install all the required packages. Run the following command in Terminal:  
    `pip install -r requirements.txt`
6. Go to the bank project
`cd bank`
7. Get the database up to date  
     `python manage.py migrate`
8. Run the following command  
    `python manage.py runserver`. 
9. Go to 127.0.0.1:8000 or localhost:8000 to run the app in a browser

By entering "localhost:8000" you will land in a page with a default database.

    
### Tests
I have written some basic tests for the functionality of the program.

If you want to run the tests you can use the following command in the terminal. Make sure you are inside the folder gruppe-33:  
    `python manage.py test`


