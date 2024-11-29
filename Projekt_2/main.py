import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error, classification_report
from sklearn.ensemble import ExtraTreesClassifier
from tpot import TPOTClassifier
from ydata_profiling import ProfileReport

data = pd.read_csv("../data/CrabAgePrediction.csv")

print(data.info())
print(data.describe())

missing_values = data.isnull().sum()
print("\nMissing values:\n" + str(missing_values))

profile = ProfileReport(data, title="Data overview", explorative=True)
profile.to_file("raport_eda.html")

data.hist(bins=20, figsize=(14, 8))
plt.suptitle("Histograms")
plt.show()

numeric_data = data.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(12, 9))
sb.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation matrix")
plt.show()

threshold_missing = 0.5 * len(data)
columns_to_remove = missing_values[missing_values > threshold_missing].index.tolist()
data = data.drop(columns=columns_to_remove)

numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numerical_columns] = data[numerical_columns].fillna(data[numerical_columns].median())

categorical_columns = data.select_dtypes(include=['object']).columns
data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

X = data.drop('Age', axis=1)
y = data['Age']
data.count(axis=1)

print(data.columns.tolist())

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=8888, stratify=y)

tpot = TPOTClassifier(generations=10, population_size=50, verbosity=2, random_state=15, n_jobs=-1)
tpot.fit(X_train, y_train)

print(tpot.fitted_pipeline_)
tpot.export("tpot_best_model.py")

y_pred = tpot.predict(X_test)
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification report:\n", classification_report(y_test, y_pred))

print("\nTraining modelu ExtraTreesClassifier...")
extratrees = ExtraTreesClassifier(
    criterion='gini',
    max_features=0.5,
    min_samples_leaf=5,
    min_samples_split=5,
    n_estimators=200,
    random_state=42
)
extratrees.fit(X_train, y_train)

y_pred_extratrees = extratrees.predict(X_test)
print("\nDokładność modelu ExtraTreesClassifier:", accuracy_score(y_test, y_pred_extratrees))
print("\nRaport klasyfikacji ExtraTreesClassifier:\n", classification_report(y_test, y_pred_extratrees))

# Zapis wyników do pliku
with open("results.txt", "w") as file:
    file.write(f"Dokładność TPOT: {accuracy_score(y_test, y_pred)}\n")
    file.write(f"Dokładność ExtraTreesClassifier: {accuracy_score(y_test, y_pred_extratrees)}\n")
    file.write(f"Raport klasyfikacji TPOT:\n{classification_report(y_test, y_pred)}\n")
    file.write(f"Raport klasyfikacji ExtraTreesClassifier:\n{classification_report(y_test, y_pred_extratrees)}\n")
