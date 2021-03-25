#Run webpage here#

from website import create_app #FROM __init__.py in folder /website

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #Automatically rerun webserver if changes are made to python code

