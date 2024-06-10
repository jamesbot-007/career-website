from flask import Flask, render_template

app = Flask(__name__)

# creating a list of dictionaries
Jobs = [
    {
        # We will give an id to each job
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Delhi, India",
        "salary": "Rs. 1,50,000"
    },
    {
        "id": 3,
        "title": "Frontend Engineer",
        "location": "Remote"
    },
    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "San Francisco, USA",
        "salary": "$150,000"
    }
]


@app.route("/")
def welcome():
  # The argument name "job" can be have any other name
  # return render_template("home2.html", jobs=Jobs, websiteName="My Carrer website")
  return render_template("home3.html", jobs=Jobs, websiteName="My Carrer website")


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
