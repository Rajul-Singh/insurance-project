from flask import Flask,render_template, request
import numpy as np
import joblib
import os
import logging

# setting logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler = logging.FileHandler('./logs/app.logs')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

webapp_root = "webapp"
static_dir = os.path.join(webapp_root,"static")
template_dir = os.path.join(webapp_root,"templates")
logger.info("template_dir linked succssfully")

model = joblib.load("models/model.joblib")
logger.info("model load successfully")

app = Flask(__name__,static_folder=static_dir, template_folder=template_dir)

@app.route("/")
def index():
    try:
        return render_template("home.html")
    except Exception as e:
        logger.error(e)

@app.route("/about")
def about():
    try:
        return render_template("about.html")
    except Exception as e:
        logger.error(e)

@app.route('/predict',methods=['POST'])
def predict():
    try:
        final_feat = list(request.form.values())
        final_feat = np.array(final_feat).reshape(1,6)
        output = model.predict(final_feat)[0]
        return render_template("predict.html",output=output)

    except Exception as e:
        logger.error(e)

if __name__ =="__main__":
    logger.info("Application running succussfully")
    app.run(debug=True)