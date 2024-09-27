from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    image_url = "https://github.com/27stephentran/Hangout_Planner/blob/main/templates/capybara.png" 
    return render_template("index_2.html", image_url = image_url)

@app.route("/input_page")
def input_page():
    return render_template("input_page.html")


if __name__ == "__main__":
    app.run()