from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
@app.route("/application", methods=['POST'])
def get_applicant_info():
    """This action obtains applicants' info and returns a submission response."""
    
    nameone = request.args.get('firstname')
    nametwo = request.args.get('lastname')
    role = request.args.get('position')
    salary = request.arges.get('amount')

    return render_template("application-response.html",
                            firstname = nameone,
                            lastname = nametwo,
                            position = role,
                            amount = salary)



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

