from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
  # return "Hello "
  return render_template("home2.html")


# open the webview in new tab and see the title of the tab is also changed.
# We set the title for the tab, apart from that we can also set the fav icon. that we see later on.

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
