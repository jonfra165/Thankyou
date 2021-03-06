#WELCOME TO THANKYOU'S READ ME FILE

1. #LINK TO PROJECT CODE FILE FOR DOWNLOAD

https://github.com/jonfra165/Thankyou.git

#SET UP

2.  (WINDOWS ONLY) You need to have MariaDB installed.
    Download link: https://mariadb.org/download/
    Follow the download and select a password you will remember (This is very important!).

    2.1 When MariaDB is downloaded you need to add a path to it. To do this follow the following steps:
        2.1.1 Copy the path to the bin-folder within the MariaDB-folder.
            Example: C:\Program Files\MariaDB 10.5\bin
        2.1.2 Open up: 'Control Panel'
        2.1.3 Choose: 'Systems'
        2.1.4 Choose: 'Advanced system setting'
        2.1.5 Choose: 'Environment Variables'
        2.1.6 In the first box choose: 'Path' 
        2.1.7 Below the first box choose: 'Edit' (DO NOT CHOOSE 'New'!)
        2.1.8 In the new window choose: 'New'
        2.1.9 Paste the path
        2.1.10 Choose 'OK' to save

    2.2. You now need to create a basic setup and the database which will be used.
        2.1 Open up Windows Powershell
        2.2 Run: mysql -u root -p
        2.3 Type in the password you chose from the download of the MariaDB-database
        2.4 Run: grant all privileges on *.* to root@localhost identified by 'password' with grant option;
        2.5 Run: CREATE DATABASE testdb;
        2.6 Run: exit;

3. (MAC ONLY) To download MariaDB on MAC follow the steps below or follow the steps in this link: https://mariadb.com/resources/blog/installing-mariadb-10-1-16-on-mac-os-x-with-homebrew/

    3.1 To download MariaDB you first need to install Xcode and Homebew, in Terminal:
        3.1.1 Run: xcode-select --install
        3.1.1 Run: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        3.1.2 Run: brew doctor (Follow on-screen instructions to fix warnings if necessary)
        3.1.3 Run: brew update

    3.2 Download MariaDB, in Terminal:
        3.2.1 Run: brew install mariadb
        3.2.2 Run: mysql_install_db
    
    3.3 You now need to secure your MariaDB installation, in Terminal:
        3.3.1 Run: mariadb-secure-installation (In case you cannot set a password in the step 3.3.1.2 go to step 3.5)
            3.3.1.1 Follow the download steps in Terminal and type in the correct settings as shown below:
                3.3.1.2 Set a root password even if the on-screen instructions tell you it is safe not to do so
                3.3.1.3 Enable unix_socket authentication? n
                3.3.1.4 Change the root password? (You can do as you want here)
                3.3.1.5 Remove anonymous users? y
                3.3.1.6 Disallow root login remotely? y
                3.3.1.7 Remove test database and access to it? (You can do as you want here)
                3.3.1.8 Reload privilege tables now? y

    3.4 You now need to create a basic setup and the database which will be used, in Terminal:
        3.4.1 Run: mariadb -u root -p 
        3.4.2 Type your chosen password
        3.4.3 Run: CREATE DATABASE testdb;
        3.4.4 Run: USE testdb;
        3.4.5 Run: GRANT ALL PRIVILEGES ON testdb TO  'root'@'localhost'  IDENTIFIED  BY  'password';
        3.4.6 Run: exit;

    3.5 In case you have NO password and cannot run mariadb-secure-installation, in Terminal:
        3.5.1 Run: mariadb
        3.5.2 Run: CREATE DATABASE testdb;
        3.5.3 Run: USE testdb;
        3.5.4 Run: GRANT ALL PRIVILEGES ON testdb TO  'root'@'localhost'  IDENTIFIED  BY  'password';
        3.5.5 Run: exit;
    
4. (WINDOWS ONLY) Before you download the required frameworks you need to add a path to your Python-folder. To do this follow the following steps: (Skip this step if you already have this path.)
    
    4.1 Copy the path to the latest python version folder within the Python-folder.
            Example: C:\Users\username\AppData\Local\Programs\Python\Python39
        4.1.1 Open up: 'Control Panel'
        4.1.2 Choose: 'Systems'
        4.1.3 Choose: 'Advanced system setting'
        4.1.4 Choose: 'Environment Variables'
        4.1.5 In the first box choose: 'Path'
        4.1.6 Below the first box choose: 'Edit' (DO NOT CHOOSE 'New'!)
        4.1.7 In the new window choose: 'New'
        4.1.9 Paste the path
        4.1.9 Choose 'OK' to save
    
    4.2 Repeat the steps above (4.1) but with a path that goes to the Scripts-folder within the latest python version folder.
        4.2.1 Example: C:\Users\username\AppData\Local\Programs\Python\Python39\Scripts

5. You will need to download the required frameworks through python's virtual environment in the project folder.

    5.1 Create a virtual environment.
        On MAC Run: python3 -m venv venv
        On WINDOWS Run: py -3 -m venv venv
        
    5.2 Activate the virtual environment.
        On MAC Run: venv/bin/activate
        On WINDOWS Run: venv\Scripts\activate

        5.2.1 (WINDOWS ONLY) If the activate command in step 5.2 generates the error-message "Activate.ps1".
            5.2.1.1 Run: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
            5.2.1.2 Repeat step 5.2 and continue on to step 5.3

    5.3 To download the required frameworks and modules.
        Run: pip install -r requirements.txt

6. Last set up steps before running the webserver.

    6.1 If you're using Visual Studio Code:
        6.1.1 Open: File
        6.1.2 Choose: Preferences
        6.1.3 Choose: Settings
        6.1.4 Type: 'json' in the search bar
        6.1.5 Under title "Launch" choose 'Edit in settings.json'
        6.1.6 Add: "python.linting.pylintArgs": ["--load-plugins", "pylint_flask"]
        6.1.7 Save and close
    
    6.2 If an error occurs, read 8.1 in section 8. 

#HOW TO RUN THE WEBSERVER

7. Run: "main.py" in project folder.

#POSSIBLE ERRORS

8. List of possible errors:

    8.1 'E1101: Instance of 'SQLAlchemy' has no 'Column' member (no-member).' 
        8.1.1 Visit this link: https://stackoverflow.com/questions/53975234/instance-of-sqlalchemy-has-no-column-member-no-member
        8.1.2 Contact us, see section 10.

#Documentation links

9. Documentation for MariaDB and Python Virtual Environment:

    9.1 MariaDB: https://mariadb.com/kb/en/documentation/
    9.2 Python Virtual Environment: https://docs.python.org/3/tutorial/venv.html
    9.3 Python Virtual Environment in Visual Studio Code: https://code.visualstudio.com/docs/python/environments

    Framework documentation:
    9.3 Flask: https://flask.palletsprojects.com/en/1.1.x/
    9.4 Flask Login: https://flask-login.readthedocs.io/en/latest/
    9.5 Flask SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/

#Contact Information

10. Contact information

    DISCORD
    10.1 ADD USER Miu#8615