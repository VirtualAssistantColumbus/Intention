from flask import Flask, send_from_directory
import os

def create_app():
    app = Flask(__name__, static_folder='static')
    
    @app.route('/')
    def index():
        return send_from_directory('static', 'index.html')
    
    @app.route('/<path:filename>')
    def static_files(filename):
        return send_from_directory('static', filename)
    
    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 