# Projet TinyML : Surveillance Intelligente et Reconnaissance des Composants
Ce projet utilise des techniques de **Machine Learning embarqué (TinyML)** pour implémenter des applications pratiques dans des environnements industriels et technologiques. Il est divisé en deux parties complémentaires qui se concentrent sur la classification des vibrations et la reconnaissance visuelle des composants électroniques.

# Partie 1 : Classification des Vibrations avec Arduino Nano 33 BLE et TensorFlow Lite
Dans cette première phase, des données de vibrations sont collectées en temps réel à l'aide du capteur IMU intégré de l'Arduino Nano 33 BLE. Ces données sont ensuite utilisées pour entraîner un modèle d'apprentissage automatique capable de classer différents types de vibrations. Une fois le modèle entraîné, il est déployé directement sur la carte Arduino pour effectuer des classifications en temps réel. Cela permet de détecter des vibrations normales ou anormales, ce qui facilite le diagnostic et la maintenance prédictive des équipements.

### Objectifs de la Partie 1 :
Collecter et analyser des données de vibrations à l'aide du capteur IMU de l'Arduino Nano 33 BLE.
Entraîner un modèle de Machine Learning avec TensorFlow Lite pour classifier les vibrations en fonction de leurs caractéristiques.
Déployer le modèle sur l'Arduino afin d’effectuer des classifications en temps réel, permettant de détecter des anomalies ou des conditions spécifiques.
# Partie 2 : Reconnaissance Visuelle des Composants avec Caméra et Node-RED
La deuxième partie du projet se concentre sur la reconnaissance visuelle des composants électroniques. À l'aide d'une caméra, des images de composants électroniques sont capturées et traitées par un modèle d'apprentissage pré-entraîné. Les résultats de classification sont ensuite envoyés vers Node-RED, un outil de développement pour l'Internet des objets (IoT), afin d'automatiser le traitement des données et d'intégrer ce système dans un environnement de contrôle plus large.

### Objectifs de la Partie 2 :
- **Capturer des images** de composants électroniques à l’aide d’une caméra.
- **Classer les images** avec un modèle pré-entraîné de classification d'images.
- **Envoyer les résultats** de la classification vers Node-RED pour des traitements automatisés, des actions en temps réel ou des analyses supplémentaires.
### Technologies Utilisées
**Arduino Nano 33 BLE** : Plateforme embarquée utilisée pour la collecte des données de vibrations et le déploiement des modèles TinyML.
**TensorFlow Lite** : Framework optimisé pour entraîner et déployer des modèles de machine learning sur des environnements embarqués.
**Caméra** : Dispositif utilisé pour capturer des images des composants électroniques.
**Node-RED** : Outil d'automatisation et de gestion des flux de données permettant d'intégrer les résultats de classification dans un système de contrôle plus large.
