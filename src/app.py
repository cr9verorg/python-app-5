from flask import Flask, jsonify
from datetime import datetime
import socket




app = Flask(__name__)

@app.route('/api/v1/info')

def info():
    return jsonify({
        'message': datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        'hostname': socket.gethostname(),
        'message2': 'This is a simple Python application running in Kubernetes!',
        'deployed_on': 'Kubernetes',
        'env': 'dev',
        'app_name': 'python-app-5'

    })

@app.route('/api/v1/healthz')

def health():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")


#'/api/v1/details'
#'/api/v1/healthz'


