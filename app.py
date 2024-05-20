from flask import Flask, request, redirect, url_for, send_from_directory,render_template
from werkzeug.utils import secure_filename
import os
from foo import FOO
app = Flask(__name__)

# Configurations
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST': 
        file = request.files['file']
        if file and allowed_file(file.filename):

            filename = secure_filename('//home//karen/Public//document//outputs//output.png')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filename = './uploads/' + filename
            foo = FOO(filename)
            foo.signature()
            # print(filename + '          ---------------------------------------------------------------------------------')
            return redirect(url_for('uploaded_file', filename='output.png'))
        

    return  render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
