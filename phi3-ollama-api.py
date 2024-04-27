from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run_phi3', methods=['POST'])
def run_phi3():
    # Check if there's input data in the request
    if not request.json or 'data' not in request.json:
        return jsonify({'error': 'No data provided'}), 400
    
    input_data = request.json['data']
    
    # Call Ollama to run the model with the input data
    try:
        # Directly pass the input data as part of the command
        result = subprocess.run(
            ["ollama", "run", "phi3", input_data], 
            capture_output=True, 
            text=True
        )
        if result.returncode != 0:
            return jsonify({'error': 'Model execution failed', 'details': result.stderr}), 500

        # Assuming the output is correctly formatted and captured
        return jsonify({'output': result.stdout})
    except Exception as e:
        return jsonify({'error': 'Failed to run the model', 'details': str(e)}), 500

if __name__ == '__main__':
    # Use the environment variable or directly set the port number
    app.run(debug=True, host='0.0.0.0', port=6000)
