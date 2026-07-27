"""
Simple Flask File Server
------------------------

This application does two things:

1. Responds to the root URL (/) with a simple text message.
2. Serves files from the current working directory using the
   /files/<filename> URL.

Example:
    If the application is started from:

        /home/bob/projects/fileserver

    and that directory contains:

        report.pdf

    then you can download it by browsing to:

        http://localhost:5000/files/report.pdf
"""

# Flask provides the web server framework.
# send_from_directory() safely serves files from a specific folder.
from flask import Flask, send_from_directory

# Standard Python module for interacting with the operating system.
import os


# ------------------------------------------------------------------
# Create the Flask application object.
#
# __name__ tells Flask where this program is located so it can
# correctly locate templates, static files, etc.
# ------------------------------------------------------------------
app = Flask(__name__)


# ------------------------------------------------------------------
# Determine the directory where the server was started.
#
# os.getcwd() returns the "current working directory", NOT necessarily
# the directory where this Python file exists.
#
# Example:
#
#     cd /home/bob/downloads
#     python3 /opt/fileserver/server.py
#
# BASE_DIR would be:
#
#     /home/bob/downloads
#
# This makes the server act like a simple file server rooted at
# whatever directory you launch it from.
# ------------------------------------------------------------------
BASE_DIR = os.getcwd()


# ------------------------------------------------------------------
# Route: /
#
# The @app.route decorator tells Flask which URL should call the
# function immediately below it.
#
# Visiting:
#
#     http://localhost:5000/
#
# executes the home() function.
# ------------------------------------------------------------------
@app.route("/")
def home():
    """
    Return a simple text message so users know the server is running.
    """
    return "Hello from Flask!"


# ------------------------------------------------------------------
# Route: /files/<path:filename>
#
# The "path:" converter allows filenames to include directories.
#
# Examples:
#
#     /files/test.txt
#     /files/images/photo.jpg
#     /files/docs/manual.pdf
#
# Without "path:", only a single filename would be accepted.
# ------------------------------------------------------------------
@app.route("/files/<path:filename>")
def serve_file(filename):
    """
    Send the requested file to the client.

    Flask's send_from_directory() is preferred over manually opening
    files because it:

    • Prevents directory traversal attacks (../)
    • Sets appropriate HTTP headers
    • Streams large files efficiently
    • Returns proper HTTP errors if the file doesn't exist

    Parameters
    ----------
    filename : str
        Relative path requested by the browser.

    Returns
    -------
    Flask Response
        The requested file or an HTTP error (404, etc.).
    """
    return send_from_directory(BASE_DIR, filename)


# ------------------------------------------------------------------
# This block only executes when this file is run directly.
#
# If this file is imported into another Python program, the code
# inside this block is NOT executed.
# ------------------------------------------------------------------
if __name__ == "__main__":

    # Start Flask's built-in development web server.
    #
    # host="0.0.0.0"
    #     Listen on every network interface instead of only localhost.
    #     This allows other machines on your LAN to connect.
    #
    # port=5000
    #     Listen on TCP port 5000.
    #
    # You can access the server from:
    #
    #     http://localhost:5000
    #
    # or from another computer:
    #
    #     http://<server-ip>:5000
    #
    # Note:
    # This built-in server is intended for development or lightweight
    # internal use. For production deployments, Flask is typically run
    # behind a WSGI server such as Gunicorn or uWSGI, often with
    # Nginx acting as a reverse proxy.
    app.run(host="0.0.0.0", port=5000)