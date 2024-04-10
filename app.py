from flask import Flask, render_template, request, make_response, jsonify
from PIL import Image

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import base64
import os

model = tf.keras.models.load_model('model.keras')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def show():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def handle():
  image = request.json['image']
  image = base64.b64decode(image.split(',')[1])

  image_path = os.path.join('./static/img', 'input.png')
  with open(image_path, 'wb') as f:
      f.write(image)

  image = Image.open(image_path)
  image = image.resize((28, 28)).convert("L")
  img_as_array = np.array(image)
  img_normalized = (img_as_array/255.0).reshape(-1, 28, 28, 1)

  plt.imshow(image, cmap='gray')
  plt.axis('off')
  plt.savefig('./static/img/input-converted.png', bbox_inches='tight', pad_inches=0)
  plt.switch_backend('agg') # to fix main thread is not in main loop
  
  result = np.argmax(model.predict(img_normalized), axis=1)[0]
  result = str(result)

  return make_response(jsonify({'result': result}))

if __name__ == "__main__":
    app.run(debug=True)