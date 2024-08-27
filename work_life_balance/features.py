# Import Dependendcies
import config
from preprocessing import categorical_columns, numerical_columns

# Import libary
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.compose import ColumnTransformer


# Load data into a dataframe
data = pd.read= pd.read_csv(config.DATA_PATH / 'interim/lifestyle.csv')

# Split training and test data set
X_train, X_test, y_train, y_test = train_test_split(
    data.drop('WORK_LIFE_BALANCE_SCORE', axis=1),
    data['WORK_LIFE_BALANCE_SCORE'],
    test_size=0.15, random_state=0)

# Mark values 'Rare' within the data with very low frequency to avoid rare cases
def value_frequency(df, var, perc):
    df = df.copy()
    temp = df.groupby(var)[var].count() / len(df)
    return temp[temp > perc].index

for column in categorical_columns:
    rare_items = value_frequency(X_train, column, 0.05)
    X_train[column] = X_train[column].where(X_train[column].isin(rare_items), 'Rare')
    X_test[column] = X_test[column].where(X_test[column].isin(rare_items), 'Rare')

# Separate different types of columns with respect to transformation
ordinal_encoding_columns = categorical_columns[:3] # These features required cardinality
one_hot_encoding_columns = categorical_columns[3:] # String categorical features
minmax_scaler_columns = numerical_columns # discrete features

column_transformer = ColumnTransformer(transformers=[
    ('label_encoder', OrdinalEncoder(), ordinal_encoding_columns),
    ('one_hot_encoder', OneHotEncoder(), one_hot_encoding_columns),
    ('minmaxscalar', MinMaxScaler(), minmax_scaler_columns)
    ], remainder='passthrough')

target_scalar = MinMaxScaler()
y_train = target_scalar.fit_transform(pd.DataFrame(y_train))

# save the column transformer and target scalar
joblib.dump(column_transformer, config.TRAIN_PATH / 'column_transformer.joblib')
joblib.dump(target_scalar, config.TRAIN_PATH / 'target_scalar.joblib')

# save data for training
joblib.dump(X_train, config.DATA_PATH / 'processed/X_train.joblib')
joblib.dump(y_train, config.DATA_PATH / 'processed/y_train.joblib')
joblib.dump(X_test, config.DATA_PATH / 'processed/X_test.joblib')
joblib.dump(y_test, config.DATA_PATH / 'processed/y_test.joblib')