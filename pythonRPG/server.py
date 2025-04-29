from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-python', methods=['GET'])
def run_python():
    try:
        # Execute the Python script and capture the output
        result = subprocess.run(['python', 'hello.py'], capture_output=True, text=True)
        return jsonify({'output': result.stdout.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)