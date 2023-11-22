from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import pandas as pd
# Load the saved model
model = load_model('stock_price_prediction_model.h5')

# Assuming df_train is your training DataFrame
scaler = MinMaxScaler()
#scaler.fit(df_train[['Open', 'Close', 'High', 'Low', 'Volume']])

#df_new = [2.0678,2.07292,2.06756,2.07192,4785.0]
df_new = pd.read_csv('Eyeofagamotto.csv')
scaler.fit(df_new[['Open', 'Close', 'High', 'Low', 'Volume']])



# Transform new data
X_new_scaled = scaler.transform(df_new[['Open', 'Close', 'High', 'Low', 'Volume']])
X_new_reshaped = X_new_scaled.reshape((X_new_scaled.shape[0], 1, X_new_scaled.shape[1]))

# Get predictions
predictions = model.predict(X_new_reshaped)

print(predictions)
