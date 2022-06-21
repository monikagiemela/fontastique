import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from keras.utils.vis_utils import plot_model
import matplotlib.pyplot as plt

from pathlib import Path
import json


TEST = Path(os.path.join("c:/","Users", "gieme", "documents", "programowanie", "oki", "fonts", "test"))
VALID = Path(os.path.join("c:/", "Users", "gieme", "documents", "programowanie", "oki", "fonts", "valid"))
TRAIN = Path(os.path.join("c:/", "Users", "gieme", "documents", "programowanie", "oki", "fonts", "train001", "train"))

batch_size = 32
img_height = 105
img_width = 105

train_ds = tf.keras.utils.image_dataset_from_directory(
  TRAIN,
  image_size=(img_height, img_width),
  batch_size=batch_size,
  labels="inferred",
  label_mode="int")

valid_ds = tf.keras.utils.image_dataset_from_directory(
  VALID,
  image_size=(img_height, img_width),
  batch_size=batch_size,
  labels="inferred",
  label_mode="int")

class_names = train_ds.class_names

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")

for image_batch, labels_batch in train_ds:
  print(image_batch.shape)
  print(labels_batch.shape)
  break

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
valid_ds = valid_ds.cache().prefetch(buffer_size=AUTOTUNE)

num_classes = len(class_names)

model = Sequential([
  layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(128, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Dropout(0.3),
  layers.BatchNormalization(),
  layers.Flatten(),
  layers.Dense(500, activation='relu'),
  layers.Dropout(0.5), 
  layers.Dense(500, activation='relu'),
  layers.Dense(num_classes, activation='softmax')
])

#optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3)
model.compile(optimizer="adam",
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.build(input_shape=(105,105,3))
model.summary()
json_config = model.to_json()
with open(os.path.join("c:/", "Users", "gieme", "Documents", "Programowanie", "oki", "fonts", "models_results", "models_architecture", 'model_3_4_architecture_bigger_dataset.json'), 'w') as fp:
  json.dump(json_config, fp)

epochs = 16 # Model 3_3 added 1 epoch
history = model.fit(
  train_ds,
  validation_data=valid_ds,
  epochs=epochs
)

model.save(os.path.join("c:/", "Users", "gieme", "Documents", "Programowanie", "oki", "fonts", "models", "my_model_3_4_bigger_dataset.h5"))

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.savefig(os.path.join("c:/", "Users", "gieme", "Documents", "Programowanie", "oki", "fonts", "models_results", "models_plots", "model_3_3_bigger_dataset_plot.png"))
plt.show()

loss, accuracy = model.evaluate(valid_ds)
print(f"Validation accuracy: {accuracy}")
print(f"Validation loss: {loss}")