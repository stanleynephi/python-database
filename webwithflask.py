from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Check if the executed file is the main program and run the app
if __name__ == "__main__":
    app.run(debug=True)
