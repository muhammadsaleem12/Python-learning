'''Problem_06 = Explore the 'Flask' module and create a web server using Flask & python.'''



from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()


# this has become a basic python server an app that prints "Hello World".