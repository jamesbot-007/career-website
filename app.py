from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
  return "Hello world"


if __name__ == "__main__":
  # if the variable __name__ has value __main__
  # This is going to be the case when we use "python app.py" command to run the file

  # print("I am code inside __name__ == '__main__' ")
  # so, if the script is invoked using the "python app.py" command then we use app.run()

  # Invoke we create an app but we not yet run the app so, invoke app.run() using that we run the flask application
  # we need to pass some options host, debug
  # when we hover on app.run() we can see the documentation. that says  set hsot=0.0.0.0 to run on the local devlopment server. and the debug=True
  app.run(host="0.0.0.0", debug=True)

# And we don't want to run the flask run command instead of that we can use the app.run() command
