import pandas as pd

df = pd.read_csv('year2008.csv')

# Create a new column for upward trend (1 if rising, 0 otherwise)
df['UpwardTrend'] = (df['Close'] > df['Close'].shift(1)).astype(int)

# Create a new column for downward trend (1 if falling, 0 otherwise)
df['DownwardTrend'] = (df['Close'] < df['Close'].shift(1)).astype(int)

df['StructureBreak'] = ((df['UpwardTrend'].shift(1) == 1) & (df['DownwardTrend'] == 1)).astype(int)
