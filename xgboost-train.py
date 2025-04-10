import xgboost as xgb
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)

model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

logging.info(f"Accuracy: {accuracy:.2f}")

model_path = Path("models")
model_path.mkdir(parents=True, exist_ok=True)
model_file = Path("models", "xgboost_model.joblib")
dump(model, model_file)





