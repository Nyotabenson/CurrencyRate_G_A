from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_streamlit')
def run_streamlit():
    subprocess.Popen(["streamlit", "run", "streamlit_app.py"])
    return "Streamlit app is running!"

if __name__ == '__main__':
    app.run(debug=True)
