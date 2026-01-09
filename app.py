from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    bg_color = os.environ.get('BG_COLOR', '#f0f9eb') # Default green background
    
    return f'''
    <html>
        <head>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: {bg_color};
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    color: #333;
                }}
                .card {{
                    background: white;
                    padding: 40px;
                    border-radius: 12px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    text-align: center;
                }}
                h1 {{ color: #2c3e50; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🐍 Python Flask App Deployed!</h1>
                <p>Hello from <b>{hostname}</b></p>
                <p>This page is served by a Python container.</p>
                <p>Status: <span style="color: green; font-weight: bold;">Operational</span></p>
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    # Important: Must listen on 0.0.0.0
    # Port 8000 matches our DockerfileGenerator configuration for Python
    app.run(host='0.0.0.0', port=8000)
