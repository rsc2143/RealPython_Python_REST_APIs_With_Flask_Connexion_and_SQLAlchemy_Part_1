from flask import (
    Flask,
    render_template
)

# Create application instance
app = Flask(__name__, template_folder="template")

# Create a URL in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:    the rendered template 'home.html'
    """
    return render_template("home.html")

# If we are running in standalone mode, then run the application
# Note that if we dont mention host='0.0.0.0' and run the Dockerfile, then it wont run as Docker wont know the host to run it on.
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
