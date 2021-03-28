#WELCOME TO THANKYOU'S READ ME FILE

1. #LINK TO PROJECT CODE FILE FOR DOWNLOAD

https://github.com/jonfra165/Thankyou.git

#REQUIREMENTS

2.  You need to have Microsoft SQL Server installed.
For more information visit: 
https://www.microsoft.com/sv-se/sql-server/sql-server-downloads

3. Additionally you will also need to install Flask, Flask SQLAlchemy, Flask login and pyodbc through python's virtual environment.

    3.1 Create a virtual environment.

        On MAC run:
        python3 -m venv venv

        On Windows run:
        py -3 -m venv venv
    
    3.2 Activate the virtual environment.

        On MAC, run:
        venv/bin/activate

        On Windows, run:
        venv\Scripts\activate.bat

    3.3 To download the required frameworks and modules, type:

        pip install -r requirements.txt

4. #POSSIBLE ERRORS

    
    4.1 (WINDOWS ONLY) If you get an error trying to download the frameworks and modules, please visit this link: 
    Hopefully a good link soon...

    4.2. If you get an error that says: "Instance of 'SQLAlchemy' has no 'Column' member (no-member)" please visit this link: 
    https://stackoverflow.com/questions/53975234/instance-of-sqlalchemy-has-no-column-member-no-member

5. #HOW TO RUN THE WEBSERVER

Run "main.py"