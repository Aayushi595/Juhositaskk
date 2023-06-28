from flask import Flask
from views import app

if __name__ == '__main__':
    app.run(port=5559,debug=True)
