"""
This module contains the main application code for a Flask web application.
It sets up the Flask app, configures it, and defines the routes for the application.
"""

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object("config.Config")


@app.route("/")
def index():
    """
    Route for the home page.

    Returns:
        A rendered template for the home page.
    """
    return render_template("index.html")


@app.route("/projects/")
def projects():
    """
    Route for the projects page.

    Returns:
        A rendered template for the projects page.
    """
    return render_template("projects.html")


@app.route("/blog/")
def blog():
    """
    Route for the blog page.

    Returns:
        A rendered template for the blog page.
    """
    return render_template("blog.html")


@app.route("/contact/")
def contact():
    """
    Route for the contact page.

    Returns:
        A rendered template for the contact page.
    """
    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(_e):
    """
    Custom error handler for 404 errors.

    Args:
        e: The exception that was raised.

    Returns:
        A rendered template for the 404 error page and a 404 status code.
    """
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
