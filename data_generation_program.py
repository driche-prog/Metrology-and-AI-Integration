### Designed by Idir DRICHE and Jérémy DELOBELLE

"""
This Python script generates random data for simulating a production environment. 
It creates synthetic data for temperature, humidity, production speed, and operator experience. 
Additionally, a defect label is assigned to each sample based on certain conditions 
(e.g., temperature above 30°C, production speed below 80 units/hour, high humidity, 
or operator experience less than 5 years). The generated data, including the defect labels, 
is then saved as a CSV file.
"""



import numpy as np
import pandas as pd

# Fixer la graine pour la reproductibilité
np.random.seed(42)

# Nombre d'exemples à générer
n_samples = 500

# Génération des données aléatoires
temperature = np.random.normal(loc=25, scale=5, size=n_samples)  # Température (moyenne = 25°C, écart-type = 5)
humidity = np.random.normal(loc=60, scale=10, size=n_samples)  # Humidité (moyenne = 60%, écart-type = 10)
production_speed = np.random.normal(loc=100, scale=20, size=n_samples)  # Vitesse de production (moyenne = 100 unités/heure, écart-type = 20)
operator_experience = np.random.randint(1, 31, size=n_samples)  # Expérience de l'opérateur (entre 1 et 30 ans)

# Créer un DataFrame avec toutes les variables
data = pd.DataFrame({
    'Température (°C)': temperature,
    'Humidité (%)': humidity,
    'Vitesse de production (unités/heure)': production_speed,
    'Expérience de l\'opérateur (années)': operator_experience
})

# Ajouter une variable cible 'Défaut' (1 pour défectueux, 0 pour bon)
def add_defect_label(row):
    # Conditions arbitraires pour générer un défaut
    if row['Température (°C)'] > 30 or row['Vitesse de production (unités/heure)'] < 80 or row['Humidité (%)'] > 75:
        return 1  # Défectueux
    elif row['Expérience de l\'opérateur (années)'] < 5:
        return 1  # Défectueux si l'opérateur a moins de 5 ans d'expérience
    else:
        return 0  # Bon

# Appliquer la fonction pour générer la variable 'Défaut'
data['Défaut'] = data.apply(add_defect_label, axis=1)

# Enregistrer les données avec la colonne 'Défaut'
file_path_with_defect = r'C:\Users\user\Music\generated_data_with_defect.csv'
data.to_csv(file_path_with_defect, index=False)

# Afficher le chemin du fichier enregistré
print(f"Les données ont été enregistrées dans : {file_path_with_defect}")
