
from tensorflow import keras
import tensorflow as tf
from keras import layers, models
import numpy as np
# 1. Load Data
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()

# 2. Preprocess: Normalize pixel values to be between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# 3. Reshape for CNN (28, 28, 1) - 1 channel for grayscale
train_images = train_images.reshape((-1, 28, 28, 1))
test_images = test_images.reshape((-1, 28, 28, 1))

# 4. Build CNN Model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5), # Regularization
    layers.Dense(10, activation='softmax') # Output layer
])

# 5. Compile and Train
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("Training model...")
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# 6. Save Model
model.save('model/fashion_model.h5')
print("Model saved as fashion_model.h5")