# Documentation du Projet TinyML
### Présentation
Ce projet vise à développer des solutions d'intelligence embarquée (TinyML) pour deux applications principales :

Classification des Vibrations : Développer un modèle TinyML capable d'analyser les données de vibrations captées par un capteur IMU (Inertial Measurement Unit) et de classer ces vibrations en temps réel sur une plateforme embarquée.
Reconnaissance des Composants Électroniques : Utilisation d'une caméra pour capturer des images de composants électroniques, classification de ces images via un modèle pré-entraîné, puis transmission des résultats vers un système d'automatisation tel que Node-RED.
# Partie 1 : Classification des Vibrations
### 1. Collecte des Données
Dans cette étape, un capteur IMU (Accéléromètre 3 axes) est utilisé pour enregistrer des données de vibrations. Ces données serviront à entraîner un modèle TinyML capable de différencier et de classer les différentes vibrations en temps réel.

**Code Arduino** : data_generation.ino
### 2. Entraînement du Modèle
Les données collectées sont ensuite utilisées pour entraîner un modèle d'apprentissage automatique. Ce modèle sera déployé sur un Arduino afin de classer les vibrations en temps réel pendant l'exécution.

**Dataset** : vibrations.csv
Ce fichier contient les données d'accélération captées par l'IMU, utilisées pour entraîner le modèle.

**Notebook d'entraînement** : training_vibrations.ipynb
Ce notebook regroupe l'intégralité du processus de prétraitement des données, l'entraînement du modèle, ainsi que l'évaluation de ses performances.

**Modèle entraîné** : vibrations_model.tflite
Une fois l'entraînement effectué, le modèle est converti en format TensorFlow Lite, afin d'être compatible avec l'Arduino.

### 3. Inférence sur Arduino
Une fois le modèle entraîné et converti au format .tflite, il est déployé sur une carte Arduino Nano 33 BLE Sense pour effectuer l'inférence en temps réel sur les vibrations captées.

**Code Arduino** : inference_vibrations.ino
Ce code permet de charger le modèle sur l'Arduino et d'effectuer l'inférence sur les données en temps réel. Les résultats de l'inférence sont affichés sur le moniteur série.
