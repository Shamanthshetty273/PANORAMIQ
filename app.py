from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import os
import cv2
from werkzeug.utils import secure_filename
from utils import loadImages
import stitch

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['RESULT_FOLDER'] = 'results/'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png'}
app.secret_key = 'your_secret_key'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if not os.path.exists(app.config['RESULT_FOLDER']):
    os.makedirs(app.config['RESULT_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def clear_uploads_folder():
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.remove(file_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_images = request.form.get('num_images', type=int)
        if num_images and num_images > 0:
            clear_uploads_folder()  # Clear the uploads folder before rendering the upload page
            return render_template('upload_images.html', num_images=num_images)
    return render_template('index.html')

@app.route('/upload-camera-image', methods=['POST'])
def upload_camera_image():
    if 'image' not in request.files:
        return 'No image file received.'

    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'Image captured and uploaded successfully.'

    return 'Failed to capture and upload image.'

@app.route('/save-uploaded-images', methods=['POST'])
def save_uploaded_images():
    num_images = request.form.get('num_images', type=int)
    if not num_images or num_images <= 0:
        return jsonify(message="Invalid number of images")

    for i in range(1, num_images + 1):
        file = request.files.get(f'image{i}')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify(message="Images saved successfully")

@app.route('/clear-uploads', methods=['POST'])
def clear_uploads():
    clear_uploads_folder()
    return jsonify(message="Uploads folder cleared")

@app.route('/complete-upload', methods=['POST'])
def complete_upload():
    num_images = request.form.get('num_images', type=int)
    if not num_images or num_images <= 0:
        return redirect(url_for('index'))

    # Check if the number of images in the upload folder matches the specified count
    uploaded_files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if allowed_file(f)]
    if len(uploaded_files) != num_images:
        return 'Error: Number of images does not match the specified count.'

    list_images = loadImages(app.config['UPLOAD_FOLDER'], resize=0)
    panorama = stitch.multiStitching(list_images)

    # Save and display result
    result_path = os.path.join(app.config['RESULT_FOLDER'], 'panorama.jpg')
    cv2.imwrite(result_path, panorama)

    return render_template('result.html', result_filename='panorama.jpg')

@app.route('/results/<filename>')
def results(filename):
    return send_from_directory(app.config['RESULT_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
