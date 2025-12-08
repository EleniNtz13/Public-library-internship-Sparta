from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# List of messages that will be displayed on the webpage
messages = ["Hello!", "Welcome!", "This is a message."]

# Define the route for the home page (localhost:5000/)
@app.route('/')
def home():
    # Join the messages with a line break so each appears on a new line
    return "<br>".join(messages)

# Start the Flask development server
if __name__ == '__main__':
    # debug=True enables automatic reload on file changes and shows errors
    app.run(debug=True)
