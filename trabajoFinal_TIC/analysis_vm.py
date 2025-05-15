# analysis_vm.py - Análisis de Datos para Máquina Virtual (VM)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Cargar datos (Iris dataset)
data = sns.load_dataset('iris')

# Exploración inicial de datos
print("\nResumen de Datos:")
print(data.describe())
print("\nDistribución de las Especies:")
print(data['species'].value_counts())

# Visualización de datos
sns.pairplot(data, hue='species')
plt.savefig("iris_pairplot_vm.png")
plt.show()

# Preparación de datos para entrenamiento
X = data.drop('species', axis=1)
y = data['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenamiento del modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluación del modelo
predictions = model.predict(X_test)
print("\nReporte de Clasificación:")
print(classification_report(y_test, predictions))

# Matriz de Confusión
cm = confusion_matrix(y_test, predictions)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=model.classes_, yticklabels=model.classes_)
plt.title("Matriz de Confusión (VM)")
plt.savefig("confusion_matrix_vm.png")
plt.show()

print("\nAnálisis completado en VM.")
