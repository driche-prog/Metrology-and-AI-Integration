### Designed by Idir DRICHE and Jérémy DELOBELLE


"""
This script loads the dataset with defect labels, created previously in the random data generation process. 
It then splits the data into training and testing sets and trains a Decision Tree classifier to predict 
the 'Défaut' (defect) based on features such as temperature, humidity, production speed, and operator experience.
The model's accuracy is calculated and displayed. Finally, the decision tree is visualized to better understand 
the decision-making process of the model.
"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Charger les données générées à partir du fichier CSV
file_path_with_defect = r'C:\Users\user\Music\generated_data_with_defect.csv'
data = pd.read_csv(file_path_with_defect)

# Séparer les variables indépendantes (X) et la variable cible (y)
X = data[['Température (°C)', 'Humidité (%)', 'Vitesse de production (unités/heure)', 'Expérience de l\'opérateur (années)']]
y = data['Défaut']

# Séparation en données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer et entraîner l'arbre de décision
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Prédictions sur le jeu de test
y_pred = clf.predict(X_test)

# Calculer la précision du modèle
accuracy = accuracy_score(y_test, y_pred)
print(f"Précision de l'arbre de décision : {accuracy:.2f}")

# Visualisation de l'arbre de décision
plt.figure(figsize=(12,8))
plot_tree(clf, feature_names=X.columns, class_names=['Bon', 'Défectueux'], filled=True, rounded=True)
plt.show()
