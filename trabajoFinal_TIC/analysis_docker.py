# analysis_vm.py - Análisis de Datos para Máquina Virtual 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import os

# Crear directorio para guardar resultados si no existe
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

# Cargar datos (Iris dataset)
data = sns.load_dataset('iris')

# Exploración inicial de datos
summary = data.describe()
species_count = data['species'].value_counts()
print("\nResumen de Datos:")
print(summary)
print("\nDistribución de las Especies:")
print(species_count)

# Guardar resumen de datos
summary.to_csv(os.path.join(RESULTS_DIR, "data_summary_vm.csv"))
species_count.to_csv(os.path.join(RESULTS_DIR, "species_count_vm.csv"))

# Visualización de datos
sns.pairplot(data, hue='species')
plt.savefig(os.path.join(RESULTS_DIR, "iris_pairplot_vm.png"))
plt.close()

# Preparación de datos para entrenamiento
X = data.drop('species', axis=1)
y = data['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenamiento del modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluación del modelo
predictions = model.predict(X_test)
report = classification_report(y_test, predictions)
cm = confusion_matrix(y_test, predictions)

# Guardar reporte de clasificación
with open(os.path.join(RESULTS_DIR, "classification_report_vm.txt"), "w") as f:
    f.write(report)

# Matriz de Confusión
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=model.classes_, yticklabels=model.classes_)
plt.title("Matriz de Confusión (VM)")
plt.savefig(os.path.join(RESULTS_DIR, "confusion_matrix_vm.png"))
plt.close()

print("\nAnálisis completado en VM. Resultados guardados en la carpeta 'results'.")
