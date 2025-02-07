from flask import Flask, render_template, url_for
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
    port = os.environ.get('PORT', 5000)  # Default to 5000 if PORT is not set
    app.run(debug=True, host='0.0.0.0', port=int(port))
    
