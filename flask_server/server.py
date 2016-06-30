# -*- coding: utf-8 -*-
from flask import Flask, request
from werkzeug import secure_filename
from pprint import pprint
import os

# refered to:
#   http://code.runnable.com/UiPcaBXaxGNYAAAL/how-to-upload-a-file-to-the-server-in-flask-for-python

app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        print 'post'
        # pprint(vars(request), depth=6)
        # print request.form.getlist
        # print request.files.getlist
        # print request.data
        # http://flask.pocoo.org/docs/0.11/api/#incoming-request-data

        num = request.form['num']
        picture = request.files['picture']
        print num
        print picture
        print picture.filename
        if picture and allowed_file(picture.filename):
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(picture.filename)
            # Move the file form the temporal folder to
            # the upload folder we setup
            picture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return 'saved'
    else:
        print 'get'
        return 'got'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

