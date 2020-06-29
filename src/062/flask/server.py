from flask import Flask


#Defining the name of our flask
app = Flask(__name__)


#Default route meaning this is the root folder of the web server
@app.route('/')
def home():
    return 'Hello World'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/blog')
def blog():
    return 'This is the blog'


#Creating a variable rule that means whenever you go to a url blog/* (number)
#It will return that vairable
#This can be an int, str, etc.
@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return "This is blog post number " + blog_id


#Note the dunder and logic saying that if name is = to main the app will run
#This starts our local hosted website
if __name__ == '__main__':
    app.run()