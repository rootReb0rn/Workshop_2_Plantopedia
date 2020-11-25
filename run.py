from flask import Flask, flash, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2
import tensorflow as tf


# physical_devices = tf.config.list_physical_devices('CPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], True)


# app = Flask(__name__, static_folder='uploads')
app = Flask(__name__)


# D Y N A M I C   O S   D I R E C T O R Y
currentDir = os.getcwd()
print(currentDir)
uploadDir = str(currentDir)+"\\static\\img\\uploads"
app.config['IMAGE_UPLOADS'] = uploadDir


# P R E P A R E  U S E R   D A T A
def prepare(filepath):
    IMG_SIZE = 100
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, 3)


# I M P O R T    M O D E L
model = tf.keras.models.load_model("model")


# P R E D I C T I O N
def returnPrediction(prediction):
    CATEGORIES = ["Bell Pepper", "Potato", "Tomato"]
    counter = 0
    for pred in prediction:
        counter = 0
        for p in pred:
            if p == 1:
                break
            else:
                counter += 1
    return str(CATEGORIES[counter])

# I N D E X   P A G E
@app.route('/')
def index():
    return render_template('index.html')


# [START]    L E A F   R E C O G N I T I O N   P A G E
@app.route('/leaf_recognition', methods=['GET', 'POST'])
def leaf_recognition_page():
    return render_template('leaf_recognition/leaf_recognition.html',currentPage='Upload')

@app.route('/leaf_recognition/upload', methods=['GET','POST'])
def leaf_upload():
    # FILE UPLOAD
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image) # VERIFICATION PURPOSE

            # STORE UPLOADED IMAGE INTO A FOLDER WHICH HAS BEEN SET
            image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))

            print("Image Saved") # VERIFICATION PURPOSE

            # [START] IMAGE RECOGNITION FUNCTION 

            # REFER LINE 24 FOR MORE DETAILS [P R E P A R E  U S E R   D A T A]
            prediction = model.predict([[prepare('static/img/uploads/'+image.filename)]]) 

            # REFER LINE 36 FOR MORE DETAILS [P R E D I C T I O N]
            prediction_with_label = returnPrediction(prediction) 
            print(prediction_with_label) # VERIFICATION PURPOSE
            
            # [END] IMAGE RECOGNITION FUNCTION 

            return render_template("leaf_recognition/leaf_recognition.html", imgPath=os.path.join(app.config['IMAGE_UPLOADS'], image.filename), imgFileName=image.filename, class_label = prediction_with_label, currentPage="Result")
    print("return")
    return redirect(url_for('leaf_recognition_page'))
# [END]      L E A F   R E C O G N I T I O N   P A G E




# [START]   T E S T I N G   E N V I R O M E N T
@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files['image']

            print(image)

            image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))

            print("Image Saved")
            print(image.filename)
            #prediction = model.predict([[prepare('uploads/'+image.filename)]])
            #prediction_with_label = returnPrediction(prediction)
            #print(prediction_with_label)
            return redirect(render_template("index.html"))

    return render_template('src/public/upload_image.html')
# [END]     T E S T I N G   E N V I R O M E N T

if __name__ == "__main__":
    app.run(debug=True)
