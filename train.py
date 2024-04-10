import tensorflow as tf
import numpy as np


(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_images, test_images = train_images/255.0, test_images/255.0

train_images_new = train_images.reshape(-1, 28, 28, 1)
test_images_new = test_images.reshape(-1, 28, 28, 1)


model_cnn = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (2, 2), input_shape = (28, 28, 1), activation = 'relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(32, (2, 2), activation = 'relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(500, activation = 'sigmoid'),
    tf.keras.layers.Dense(10, activation = 'softmax')
])

model_cnn.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
  )

results_cnn = model_cnn.fit(
    train_images, train_labels,
    epochs = 20, batch_size = 1000,
    validation_data = (test_images, test_labels)
)

model_cnn.save('model.keras')