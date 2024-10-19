from flask import Flask , jsonify
from config import Config


app = Flask(__name__) 
app.config.from_object(Config)

@app.route('/')
def home():
    return jsonify(message="This will be the Home_page!!")

if __name__ == "__main__":
    app.run(debug=True)