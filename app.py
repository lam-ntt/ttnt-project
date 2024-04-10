from flask import Flask, render_template, request
from PIL import Image

import tensorflow as tf
import numpy as np
import base64
import os

app = Flask(__name__)

model = tf.keras.models.load_model('model.keras')

@app.route('/', methods = ['GET'])
def show():
  return render_template('index.html')

@app.route('/', methods = ['POST'])
def handle():
  image = request.json['image']
  image = base64.b64decode(image.split(',')[1])

  image_path = os.path.join('static/img', 'test.png')
  with open(image_path, 'wb') as f:
      f.write(image)

  image = Image.open(image_path)
  image = image.resize((28, 28)).convert("L")
  img_as_array = (np.array(image)/255.0).reshape(-1, 28, 28, 1)

  image_path = os.path.join('static/img', 'test2.png')
  with open(image_path, 'wb') as f:
      f.write(img_as_array) 
  
  result = np.argmax(model.predict(img_as_array), axis=1)[0]

  print(result)

  tmp = str(result)
  tmp = 'Lam'

  return render_template('index.html', tmp=tmp)


if __name__ == "__main__":
    app.run(debug=True)