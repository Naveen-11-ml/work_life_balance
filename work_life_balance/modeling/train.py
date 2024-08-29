# Import dependendcies
import work_life_balance.config as config

# Import libary
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, root_mean_squared_error, mean_absolute_error, r2_score
import joblib
import pandas as pd

# Load data and transformer for processing
column_transformer = joblib.load(config.TRANSFORMER_PATH/ 'column_transformer.joblib')
target_scalar = joblib.load(config.TRANSFORMER_PATH / 'target_scalar.joblib')
X_train = joblib.load(config.DATA_PATH / 'processed/X_train.joblib')
y_train = joblib.load(config.DATA_PATH / 'processed/y_train.joblib')
X_test = joblib.load(config.DATA_PATH / 'processed/X_test.joblib')
y_test = joblib.load(config.DATA_PATH / 'processed/y_test.joblib')

# Create model pipeline
pipeline = Pipeline([('preprossing', column_transformer),
                    ('ensemble', HistGradientBoostingRegressor())])

# Train the model
pipeline.fit(X_train, y_train)


y_pred = pipeline.predict(X_test)

mse = mean_squared_error(target_scalar.transform(pd.DataFrame(y_test)), y_pred)
rmse = root_mean_squared_error(target_scalar.transform(pd.DataFrame(y_test)), y_pred)
mbe = mean_absolute_error(target_scalar.transform(pd.DataFrame(y_test)), y_pred)
r2 = r2_score(target_scalar.transform(pd.DataFrame(y_test)), y_pred)

if rmse > 0.1 or mbe >0.1 or r2 < 0.9:
    raise Exception("Retrain the Model")

# Save model for prediction
joblib.dump(pipeline, config.MODEL_PATH / 'model-v1.joblib')