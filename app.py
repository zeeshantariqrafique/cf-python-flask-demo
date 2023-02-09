import os
import flask


app = flask.Flask(__name__)
port = os.getenv("PORT")

@app.route('/')
def context_root():
    return "Welcome to my dummy flask app"

def main():
    app.run()

if __name__ == "__main__":
    main()