#WELCOME TO THANKYOU'S READ ME FILE

1. #LINK TO PROJECT CODE FILE FOR DOWNLOAD

https://github.com/jonfra165/Thankyou.git

#REQUIREMENTS

2.  You need to have Microsoft SQL Server installed.
For more information visit: https://www.microsoft.com/sv-se/sql-server/sql-server-downloads

3. Additionally you will also need to install Flask, Flask SQLAlchemy, Flask login and pyodbc through python's virtual environment.

    3.1 If there is no existing folder called 'venv' in this directory, it will need to be created.

        To create a 'venv' folder on MAC run:
        python3 -m venv venv

        To create a 'venv' folder on Windows run:
        py -3 -m venv venv
    
    3.2 If there is an existing folder called 'venv' in this directory, you will have to activate it.

        To activate the virtual environment on MAC, run:
        venv/bin/activate

        To activate the virtual environment on Windows, run:
        venv\Scripts\activate.bat

    3.3 To download the required frameworks and modules, type:

        pip install -r requirements.txt

4. #POSSIBLE ERRORS

If you get an error that says: "Instance of 'SQLAlchemy' has no 'Column' member (no-member)" please visit this link: https://stackoverflow.com/questions/53975234/instance-of-sqlalchemy-has-no-column-member-no-member

5. #HOW TO RUN THE WEBSERVER

Run "main.py"