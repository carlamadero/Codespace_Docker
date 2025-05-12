import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Cargar el dataset Iris
df = pd.DataFrame(load_iris().data, columns=load_iris().feature_names)
df['species'] = load_iris().target

# Dividir en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    df.drop('species', axis=1), df['species'], test_size=0.3, random_state=42
)

# Entrenar el modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluar el modelo
predictions = model.predict(X_test)
print("\n=== Reporte de Clasificación ===")
print(classification_report(y_test, predictions))

# Matriz de confusión
cm = confusion_matrix(y_test, predictions)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Matriz de Confusión - Random Forest")
plt.xlabel("Predicción")
plt.ylabel("Actual")
plt.show()

# Importancia de características
importance = model.feature_importances_
features = df.drop('species', axis=1).columns
sns.barplot(x=importance, y=features)
plt.title("Importancia de Características")
plt.show()