from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Hello from your Dockerized Python app!"

if __name__ == '__main__':
    # Important: use host='0.0.0.0' so Docker can expose it
    app.run(host='0.0.0.0', port=3000)
