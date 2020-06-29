from flask import Flask


#Defining the name of our flask
app = Flask(__name__)


#Default route meaning this is the root folder of the web server
@app.route('/')
def home():
    return 'Hello World'


#Note the dunder and logic saying that if name is = to main the app will run
#This starts our local hosted website
if __name__ == '__main__':
    app.run()