import pandas as pd
# Calculate PriceDifference
df['PriceDifference'] = df['Close'] - df['Close'].shift(1)

# Identify UpwardTrend and DownwardTrend
df['UpwardTrend'] = (df['PriceDifference'] > 0.0001).astype(int)
df['DownwardTrend'] = (df['PriceDifference'] < -0.0001).astype(int)

# Use rolling windows to check the previous 5 and next 5 candles
window_size = 5

# Previous 5 candles
df['PrevUpwardTrend'] = df['UpwardTrend'].rolling(window=window_size).sum().shift(1)
df['PrevDownwardTrend'] = df['DownwardTrend'].rolling(window=window_size).sum().shift(1)

# Next 5 candles
df['NextUpwardTrend'] = df['UpwardTrend'].rolling(window=window_size).sum().shift(-window_size)
df['NextDownwardTrend'] = df['DownwardTrend'].rolling(window=window_size).sum().shift(-window_size)

# Identify StructureBreak based on the absolute value of PriceDifference
df['StructureBreak'] = (df['PriceDifference'].abs() >= 0.0001).astype(int)

# Drop intermediate columns if needed
df = df.drop(['PrevUpwardTrend', 'PrevDownwardTrend', 'NextUpwardTrend', 'NextDownwardTrend'], axis=1)

# Print or use df as needed
print(df)
