
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/api/v1/resource', methods=['GET'])
def get_resource():
    return jsonify({"message": "Hello, World!"})
if __name__ == '__main__':
    app.run(debug=True)
