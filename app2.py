from flask import Flask, jsonify, render_template
app = Flask(__name__)
Jobs = [
    {
   
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
        "salary": "$60,000"
    }
]


@app.route("/")
def welcome():
  return render_template("home3.html", jobs=Jobs, websiteName="My Carrer website")


@app.route("/jobs")
def list_jobs():
    return jsonify(Jobs)
    # open the webview in new tab add "/about" at the end and you can see we have sent the data as JSON

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
