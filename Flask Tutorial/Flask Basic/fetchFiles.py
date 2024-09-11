from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'files')

@app.route("/")
def upload():
    return render_template('upload-files.html')

@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        try:
            f = request.files['file']
            file_path = os.path.join(UPLOAD_FOLDER, f.filename)
            f.save(file_path)
            return f'File uploaded successfully and saved to {file_path}'
        except PermissionError as e:
            return f'Permission error: {e}', 500
        except Exception as e:
            return f'An error occurred: {e}', 500

if __name__ == "__main__":
    app.run(debug=True)
