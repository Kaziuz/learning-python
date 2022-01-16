""""
En este script vamos a hacer una regresión para encontrar
la relación entre celius y fahrenheit
Para correr el script en spider, shift + enter
"""

import tensorflow as tf           # Nos permite crear redes RNA
import pandas as pd               # Nos permite manipular set de datos
import numpy as np                # Hacer matematica y matrices
import seaborn as sns             # Hacer visualizaciones
import matplotlib.pyplot as plt   # Hacer plots o graficos de los datos

# Cargamos los datos
temperature_df = pd.read_csv('data.csv')

# Visualizamos los datos
sns.scatterplot(temperature_df['celsius'], temperature_df['fahrenheit'])

# Creamos un set de datos de entrenamiento basado en los datos 
# cargados previamente
x_train = temperature_df['celsius']
y_train = temperature_df['fahrenheit']

# Creamos el modelo
# keras es una api escrita en python para deep learning
model = tf.keras.Sequential()
# significa que crearemos nuestro modelo
# de manera sequencial, capa por capa

# primera capa neuronal de solo 1 neurona
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

# print("version de tensorflow ".format(tf.__version__))
# Esto nos imprime un resumen del modelo, poder ver la red antes de empezar a trabajar con ella
# model.summary()

# Compilado
# aqui es donde va la funcion de perdida
#model.compile(optimizer=tf.keras.optimizers.Adam(0.5), loss='mean_squared_error')

# Cuando el modelo se acerca al resultado, podemos subir un poquito
# el valor del adam para ajustar el entrenado
model.compile(optimizer=tf.keras.optimizers.Adam(1), loss='mean_squared_error')

# Entrenado del modelo
# un epoch es una iteración a la data de entrenamiento
epochs_hist = model.fit(x_train, y_train, epochs=100)

# Corremos esta linea para que nos de las llaves del epoch_hist
epochs_hist.history.keys()

# Graficamos el historial de entrenamiento
plt.plot(epochs_hist.history['loss'])
plt.title('Progreso de perdida durante el entrenamiento del modelo')
plt.xlabel('Epoch')
plt.ylabel('Training loss')
plt.legend('Training loss')

# Estos son los pesos de nuestra modelo
model.get_weights()

# Predicciones
temp_C = 2
temp_F = model.predict([temp_C])
print('Los {} celsius equivalen a {} fahrenheit'.format(temp_C, temp_F))





