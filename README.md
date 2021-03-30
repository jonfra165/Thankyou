#WELCOME TO THANKYOU'S READ ME FILE

1. #LINK TO PROJECT CODE FILE FOR DOWNLOAD

https://github.com/jonfra165/Thankyou.git

#SET UP

2.  (WINDOWS ONLY) You need to have MariaDB installed.
    Download link: https://www.microsoft.com/sv-se/sql-server/sql-server-downloads
    Follow the download set up? and select a password you will remember (This is very important!).

    2.1 When MariaDB is downloaded you noew need to add a path to it. To do this follow the following steps:
        2.1.1 Copy the path to the bin-folder within the MariaDB-folder.
            Example: C:\Program Files\MariaDB 10.5\bin
        2.1.2 Open up 'Control Panel'
        2.1.3 Choose 'Systems'
        2.1.4 Choose 'Advanced system setting'
        2.1.5 Choose 'Environment Variables'
        2.1.6 In the first box, choose 'Path' and then click 'Edit' below this box.
        2.1.7 Choose 'New'
        2.1.8 Paste the path
        2.1.9 Choose 'OK' to save

    2.2. You now need to create a basic setup and the database which will be used.
        
        2.1 Open up Windows Powershell
        2.2 Run: mysql -u root -p
        2.3 Type in the password you chose from the download of the MariaDB-database
        2.4 Run: grant all privileges on *.* to root@localhost identified by 'password' with grant option;
        2.5 Run: CREATE DATABASE testdb;
        2.6 Run: exit;

3. (MAC ONLY) To download MariaDB on MAC this follow the following steps: [TO BE TESTED]

    3.1 Download Homebew by opening Terminal and run: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    3.2 The next step is to download MariaDB in the same terminal
        3.2.1 Run: brew install mariadb
        3.2.2 Follow the steps in the terminal.
    
    3.3 You now need to create a basic setup and the database which will be used, in the same terminal.
        3.3.2 Run: mysql.server start
        3.3.3 Run: mysql
        3.3.4 Type in the password you chose from the download of the MariaDB-database
        3.3.5 Run: grant all privileges on *.* to root@localhost identified by 'password' with grant option;
        3.3.6 Run: CREATE DATABASE testdb;
        3.3.7 Run: exit;
    
4. (WINDOWS ONLY) Before you download the required frameworks you need to add a path to your Python-folder. To do this follow the following steps: (Skip this step if you already have this path.)
    
    4.1 Copy the path to the Python39-folder within the Python-folder.
            Example: C:\Users\username\AppData\Local\Programs\Python\Python39
        4.1.2 Open up 'Control Panel'
        4.1.3 Choose 'Systems'
        4.1.4 Choose 'Advanced system setting'
        4.1.5 Choose 'Environment Variables'
        4.1.6 In the first box, choose 'Path' and then click 'Edit' below this box.
        4.1.7 Choose 'New'
        4.1.8 Paste the path
        4.1.9 Choose 'OK' to save
    
    4.2 Repeat the steps above but with a path that goes to the Scripts-folder within the Python39-folder.
        4.2.1 Example: C:\Users\username\AppData\Local\Programs\Python\Python39\Scripts

5. You will need to download the required frameworks through python's virtual environment.

    5.1 Create a virtual environment.
        On MAC run: python3 -m venv venv
        On WINDOWS run: py -3 -m venv venv
        
    5.2 Activate the virtual environment.
        On MAC, run: venv/bin/activate
        On WINDOWS, run: venv\Scripts\activate.bat

    5.3 To download the required frameworks and modules, run: pip install -r requirements.txt

6. Last set up steps before running the webserver.

    6.1 If you're using Visual Studio Code:
        6.1.1 Open: File
        6.1.2 Choose: Preferences
        6.1.3 Choose: Settings
        6.1.4 Type: Json in the search bar
        6.1.5 Under title "Launch", choose 'Edit in settings.son'
        6.1.6 Add: "python.linting.pylintArgs": ["--load-plugins", "pylint_flask"]
        6.1.7 Save and close
    
    6.2 If you're using another code editor else and you get an error that says: E1101: Instance of 'SQLAlchemy' has no 'Column' member (no-member). 
        6.2.1 Contact us via discord: [ADD SOMETHING TO THIS LATER]
        6.2.2 Visit this link: https://stackoverflow.com/questions/53975234/instance-of-sqlalchemy-has-no-column-member-no-member

#POSSIBLE ERRORS

######################################

6. #HOW TO RUN THE WEBSERVER

Run "main.py"