from flask import Flask, render_template
import os

def create_app():
    app = Flask(__name__, static_folder='static')
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/mission')
    def mission():
        return render_template('mission.html')
    
    @app.route('/contribute')
    def contribute():
        return render_template('contribute.html')
    
    @app.route('/status')
    def status():
        return render_template('status.html')
    
    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)