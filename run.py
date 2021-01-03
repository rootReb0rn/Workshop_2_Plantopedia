from flask import Flask, flash, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2
import tensorflow as tf
from experta import *
from es_dic_plant import *
import numpy as np

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)


app = Flask(__name__)


# D Y N A M I C   O S   D I R E C T O R Y
currentDir = os.getcwd()
print(currentDir)
uploadDir = str(currentDir)+"\\static\\img\\uploads"
app.config['IMAGE_UPLOADS'] = uploadDir

# [START]   L E A F   R E C O G N I T I O N   U S I N G    C N N 

# P R E P A R E  U S E R   D A T A
def prepare(filepath):
    IMG_SIZE = 200
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    new_array = np.array(new_array/255.0)
    return new_array.reshape(-1, IMG_SIZE,IMG_SIZE, 3)


# I M P O R T    M O D E L
model = tf.keras.models.load_model("model")


# P R E D I C T I O N
def returnPrediction(prediction):
    CATEGORIES = ["Lemon", "Mango", "Noni"]
    max = np.argmax(prediction)
    return str(CATEGORIES[max])

# [END]    L E A F   R E C O G N I T I O N   U S I N G    C N N 

#-----------------------------------------------------------------------------------------------------

# [START]   EXPERT SYSTEM

# LEMON
TOTAL_QUESTION_LEMON = 10

DISEASE_01_LEMON = ['no','no','no','yes','yes','no','no','no','no','no']      # Citrus Canker
DISEASE_02_LEMON = ['no','no','no','no','no','no','no','yes','yes','yes']     # Citrus Leaf Miner
DISEASE_03_LEMON = ['yes','yes','yes','no','no','no','no','no','no','no']     # Lemon Anthracnose
DISEASE_04_LEMON = ['yes','no','no','no','no','yes','yes','no','no','no']     # Lemon Huanglongbing

DISEASE_POPULATION_LEMON = [DISEASE_01_LEMON,DISEASE_02_LEMON,DISEASE_03_LEMON,DISEASE_04_LEMON]

# MANGO
TOTAL_QUESTION_MANGO = 8

DISEASE_01_MANGO = ['yes','yes','no','no','no','no','no','no']      # Algal Leaf Spot
DISEASE_02_MANGO = ['no','no','no','no','no','no','yes','yes']      # Phoma Blight
DISEASE_03_MANGO = ['no','no','yes','yes','no','no','no','no']      # Powdery Mildew
DISEASE_04_MANGO = ['no','no','no','no','yes','yes','no','no']      # Sooty Mold

DISEASE_POPULATION_MANGO = [DISEASE_01_MANGO,DISEASE_02_MANGO,DISEASE_03_MANGO,DISEASE_04_MANGO]

# NONI
TOTAL_QUESTION_NONI = 11

DISEASE_01_NONI = ['no','no','no','yes','yes','no','no','no','no','no','no']      # Algal Leaf Spot
DISEASE_02_NONI = ['no','no','no','no','no','no','no','no','yes','yes','yes']     # Heliothrips Haemorrhoidalis
DISEASE_03_NONI = ['no','no','no','no','no','yes','yes','yes','no','no','no']     # Noni Anthracnose
DISEASE_04_NONI = ['yes','yes','yes','no','no','no','no','no','no','no','no']     # Noni Black Flag

DISEASE_POPULATION_NONI = [DISEASE_01_NONI,DISEASE_02_NONI,DISEASE_03_NONI,DISEASE_04_NONI]

# K N O W L E D G E   E N G I N E
def InferenceEnginePlant(user_input,plant_type):

    result = " "
    if(plant_type == 'Lemon'):
        plant_Lemon.reset()
        plant_Lemon.declare(Symptom(ques1=user_input[0]),Symptom(ques2=user_input[1]),Symptom(ques3=user_input[2]),Symptom(ques4=user_input[3]),Symptom(ques5=user_input[4]),Symptom(ques6=user_input[5]),Symptom(ques7=user_input[6]),Symptom(ques8=user_input[7]),Symptom(ques9=user_input[8]),Symptom(ques10=user_input[9]))
        plant_Lemon.run()
        #print(plant_Lemon.response)
        result = plant_Lemon.response
    elif(plant_type == 'Mango'):
        plant_Mango.reset()
        plant_Mango.declare(Symptom(ques1=user_input[0]),Symptom(ques2=user_input[1]),Symptom(ques3=user_input[2]),Symptom(ques4=user_input[3]),Symptom(ques5=user_input[4]),Symptom(ques6=user_input[5]),Symptom(ques7=user_input[6]),Symptom(ques8=user_input[7]))
        plant_Mango.run()
        #print(plant_Mango.response)
        result = plant_Mango.response
    elif(plant_type == 'Noni'):
        plant_Noni.reset()
        plant_Noni.declare(Symptom(ques1=user_input[0]),Symptom(ques2=user_input[1]),Symptom(ques3=user_input[2]),Symptom(ques4=user_input[3]),Symptom(ques5=user_input[4]),Symptom(ques6=user_input[5]),Symptom(ques7=user_input[6]),Symptom(ques8=user_input[7]),Symptom(ques9=user_input[8]),Symptom(ques10=user_input[9]),Symptom(ques11=user_input[10]))
        plant_Noni.run()
        #print(plant_Noni.response)
        result = plant_Noni.response
    else:
        print("Not Match Found on Inference Engice Plant Function")

    return result

# C O N F I D E N C E   L E V E L
def confidence_level(user_input,DISEASE_POPULATION,TOTAL_QUESTION,plant_type):
    DISEASE_CONFINDENCE = []
    count_confidence_level = 0
    find_index = 0
    final_user_input = []
    result = " "
    percentage = 0.0;


    for test in DISEASE_POPULATION:
        print("------------------------------------")
        count_confidence_level = 0
        print(test)
        for(a,b) in zip(test,user_input):
            if(a == b):
                count_confidence_level = 1 + count_confidence_level
                print("MATCH")
            else:
                print("NOT MATCH")
                
        DISEASE_CONFINDENCE.append(count_confidence_level/TOTAL_QUESTION)
    
        print(count_confidence_level)
        print(count_confidence_level/TOTAL_QUESTION)


    print("------------------------------------")


    find_index = DISEASE_CONFINDENCE.index(max(DISEASE_CONFINDENCE))

    if((max(DISEASE_CONFINDENCE)) == 1.0):
        print("100% Match")
        result = InferenceEnginePlant(user_input,plant_type)
        percentage = 100

    else:
        if((max(DISEASE_CONFINDENCE)) < 1.0):
            if((max(DISEASE_CONFINDENCE)) >= 0.6):
                for s in DISEASE_POPULATION[find_index]:
                    final_user_input.append(s)
                result = InferenceEnginePlant(final_user_input,plant_type)
                percentage = DISEASE_CONFINDENCE[find_index]*100
                print(str(percentage) + "% MATCH")
                print("Execute the rule")
            else:
                result = InferenceEnginePlant(user_input,plant_type)
                percentage = 0
        else:
           result = InferenceEnginePlant(user_input,plant_type)
           percentage = 0

    return result,percentage

# [END]     EXPERT SYSTEM

#-----------------------------------------------------------------------------------------------------

# I N D E X   P A G E
@app.route('/')
def index():
    return render_template('index.html')

#-----------------------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------------------

# [START]   P L A N T   D I S E A S E   A D V I C E
@app.route('/plant_disease_advice')
def plant_disease_advice_page():
    return render_template('plant_disease_advice/plant_disease_advice.html')

@app.route('/plant_disease_advice/lemon', methods=['GET', 'POST'])
def plant_disease_lemon_page():
    if request.method == 'POST':
        user_input_lemon = []
        result = " "
       
        value1 = request.form['ques1']
        value2 = request.form['ques2']
        value3 = request.form['ques3']
        value4 = request.form['ques4']
        value5 = request.form['ques5']
        value6 = request.form['ques6']
        value7 = request.form['ques7']
        value8 = request.form['ques8']
        value9 = request.form['ques9']
        value10 = request.form['ques10']
        user_input_lemon.append(value1)
        user_input_lemon.append(value2)
        user_input_lemon.append(value3)
        user_input_lemon.append(value4)
        user_input_lemon.append(value5)
        user_input_lemon.append(value6)
        user_input_lemon.append(value7)
        user_input_lemon.append(value8)
        user_input_lemon.append(value9)
        user_input_lemon.append(value10)
        
        print(user_input_lemon)

        result,percentage = confidence_level(user_input_lemon,DISEASE_POPULATION_LEMON,TOTAL_QUESTION_LEMON,'Lemon')
        return render_template('plant_disease_advice/Lemon/lemonResult.html',ques1=user_input_lemon[0],ques2=user_input_lemon[1],ques3=user_input_lemon[2],ques4=user_input_lemon[3],ques5=user_input_lemon[4],ques6=user_input_lemon[5],ques7=user_input_lemon[6],ques8=user_input_lemon[7],ques9=user_input_lemon[8],ques10=user_input_lemon[9],viewData=result,confidencePercentage=percentage)

    return render_template('plant_disease_advice/Lemon/lemonES.html')

@app.route('/plant_disease_advice/mango', methods=['GET','POST'])
def plant_disease_mango_page():
    if request.method == "POST":
        user_input_mango = []
        resultMango = " "
        user_input_mango.append(request.form['ques1'])
        user_input_mango.append(request.form['ques2'])
        user_input_mango.append(request.form['ques3'])
        user_input_mango.append(request.form['ques4'])
        user_input_mango.append(request.form['ques5'])
        user_input_mango.append(request.form['ques6'])
        user_input_mango.append(request.form['ques7'])
        user_input_mango.append(request.form['ques8'])
        print(user_input_mango)

        result,percentage = confidence_level(user_input_mango,DISEASE_POPULATION_MANGO,TOTAL_QUESTION_MANGO,'Mango')
        return render_template('plant_disease_advice/Mango/mangoResult.html',viewData=result,confidencePercentage=percentage)
    
    return render_template('plant_disease_advice/Mango/mangoES.html')


@app.route('/plant_disease_advice/noni', methods=['GET','POST'])
def plant_disease_noni_page():
    if request.method == "POST":
        user_input_noni = []
        resultNoni = " "
        user_input_noni.append(request.form['ques1'])
        user_input_noni.append(request.form['ques2'])
        user_input_noni.append(request.form['ques3'])
        user_input_noni.append(request.form['ques4'])
        user_input_noni.append(request.form['ques5'])
        user_input_noni.append(request.form['ques6'])
        user_input_noni.append(request.form['ques7'])
        user_input_noni.append(request.form['ques8'])
        user_input_noni.append(request.form['ques9'])
        user_input_noni.append(request.form['ques10'])
        user_input_noni.append(request.form['ques11'])
        print(user_input_noni)

        result,percentage = confidence_level(user_input_noni,DISEASE_POPULATION_NONI,TOTAL_QUESTION_NONI,'Noni')
        return render_template('plant_disease_advice/Noni/noniResult.html',viewData=result,confidencePercentage=percentage)
    
    return render_template('plant_disease_advice/Noni/noniES.html')

# [END]     P L A N T   D I S E A S E   A D V I C E

#-----------------------------------------------------------------------------------------------------

# [START]   P L A N T   I N F O R M A T I O N   P A G E
@app.route('/plant_information')
def plant_information_page():
    return render_template('plant_information/plant_information.html')

@app.route('/plant_information/lemon')
def lemon_page():
    return render_template('plant_information/Lemon/lemon.html')

@app.route('/plant_information/mango')
def mango_page():
    return render_template('plant_information/Mango/mango.html')

@app.route('/plant_information/noni')
def noni_page():
    return render_template('plant_information/Noni/noni.html')

# [END]     P L A N T   I N F O R M A T I O N   P A G E 

#-----------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True)
