from flask import Flask, request, jsonify
import os
from utils.resume_parser import parse_resume

app = Flask(__name__)

# Directory to save uploaded resumes
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files.get("resume")
    
    if uploaded_file and uploaded_file.filename.endswith('.pdf'):
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(file_path)
        
        # Parse the resume
        response = parse_resume(file_path)

        # Return the parsed data as JSON
        return jsonify(response)  # Send response as JSON
    
    return jsonify({"error": "Invalid file format. Please upload a PDF file."}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
