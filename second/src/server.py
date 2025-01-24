from flask import Flask, render_template
from re import match
import os

app = Flask(__name__)
app.template_folder = os.path.join(os.path.dirname(__file__), "templates")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register/<string:email>', methods=['GET'])
def register(email: str):
    response = write_email(email)
    return render_template("response.html", email=email, response=response)

def write_email(email: str):
    # Email regex for validation
    email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not match(email_regex, email):
        return "Email invalid"

    # Path to the emails file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    email_file_path = os.path.join(current_dir, "emails.txt")

    # Write to the emails file
    with open(email_file_path, "r+") as email_file:
        emails = [line.strip() for line in email_file.readlines()]
        if email in emails:
            return "Email already registered"

        email_file.write(email + "\n")
    return "Email registered"

if __name__ == "__main__":
    app.run(debug=True)