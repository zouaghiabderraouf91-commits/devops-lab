from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1> 🚀 DevOps Lab v3 — CI/CD Works!</h1>
    <p>Container is running!</p>
    <p>Hostname: ''' + os.popen('hostname').read() + '''</p>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
