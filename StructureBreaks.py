import pandas as pd
import plotly.graph_objects as go

# Loading dataset
df = pd.read_csv('year2008.csv')

# Calculate PriceDifference
df['PriceDifference'] = df['Close'] - df['Close'].shift(1)

# Identify UpwardTrend and DownwardTrend
df['UpwardTrend'] = (df['PriceDifference'] > 0.0001).astype(int)
df['DownwardTrend'] = (df['PriceDifference'] < -0.0001).astype(int)

# Identify StructureBreak and the direction of the trend
df['StructureBreak'] = (df['UpwardTrend'].shift(1) != df['UpwardTrend']) | (df['DownwardTrend'].shift(1) != df['DownwardTrend'])
df['TrendDirection'] = df['UpwardTrend'].map({1: 'Up', 0: ''}) + df['DownwardTrend'].map({1: 'Down', 0: ''})

# Filter rows where StructureBreak is 1
break_points = df[df['StructureBreak']]

# Create a candlestick chart with Plotly
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                name='Candlesticks')])

# Define padding values
upward_padding = -0.05  # Adjust this value to control the padding for upward trends
downward_padding = 0.05  # Adjust this value to control the padding for downward trends

# Add trace for Structure Break with different markers based on trend direction
for direction in ['Up', 'Down']:
    trend_points = break_points[break_points['TrendDirection'].str.contains(direction)]
    if direction == 'Up':
        marker_style = dict(symbol='triangle-up', size=12)
        y_coords = trend_points['Close'] + upward_padding
    else:
        marker_style = dict(symbol='triangle-down-open', size=12)
        y_coords = trend_points['Close'] + downward_padding
        
    fig.add_trace(go.Scatter(x=trend_points['Date'], y=y_coords,
                             mode='markers',
                             marker=marker_style,
                             name=f'{direction}ward Trend Structure Break'))

# Show the plot
fig.update_layout( title='Candlestick Chart with Structure Break Points and Trend Markers',
    
    autosize=False,
    width=1200,
    height=1000,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    paper_bgcolor="LightSteelBlue",
    
)
fig.update(layout_xaxis_rangeslider_visible=False)
fig.show()
