from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def landpage():
    return render_template('landpage_oficial.html')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)