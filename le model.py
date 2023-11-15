from tensorflow.keras.models import load_model

# Load the saved model
loaded_model = load_model('stock_price_prediction_model.h5')


# Make predictions on new data
# Suppose df_new is your new DataFrame containing the data for prediction
X_new_scaled = scaler.transform(df_new[['Open', 'Close', 'High', 'Low', 'Volume']])
X_new_reshaped = X_new_scaled.reshape((X_new_scaled.shape[0], 1, X_new_scaled.shape[1]))

# Predict the 'Close' values
predictions_new = model.predict(X_new_reshaped)

#2.0678,2.07292,2.06756,2.07192,4785.0

# The 'predictions_new' variable now contains the predicted 'Close' values for the new data.