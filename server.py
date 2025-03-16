// filepath: c:\projects\pythonai\functions\server.py
import os
from flask import Flask, request, send_from_directory
import gradio as gr
from gradiant import demo  # Import your Gradio app

app = Flask(__name__, static_folder="public")

@app.route("/", methods=["GET"])
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/.netlify/functions/server", methods=["GET", "POST"])
def server():
    return demo.launch(share=True)

if __name__ == "__main__":
    app.run()