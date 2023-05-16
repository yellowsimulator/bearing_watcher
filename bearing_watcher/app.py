import dash
import pandas as pd
import numpy as np
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from glob import glob
import re
from pathlib import Path

from demodulation import get_envelope_spectrum

def sort_key(file):
    # sort files by the number in their name
    number = int(re.search(r'(\d+)', str(file)).group(1))
    return number

# Sort the files using the custom sorting function
file_paths = Path('vibration')
files = file_paths.glob('*.parquet')
sorted_files = sorted(files, key=sort_key)

# Initialize the app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div(style={'backgroundColor': '#111111'}, children=[
    html.H1(
        children='Vibration Signal Analysis',
        style={
            'textAlign': 'center',
            'color': '#7FDBFF'
        }
    ),

    html.Div(children='Select a file:', style={
        'color': '#7FDBFF'
    }),

   dcc.Dropdown(
    id='file-dropdown',
    # Create an option for each file
    options=[{'label': str(file), 'value': str(file)} for file in sorted_files],
    value=str(sorted_files[0]) if files else None
    ),

    dcc.Graph(
        id='frequency-spectrum',
        config={
            'displayModeBar': False
        }
    ),

    dcc.Graph(
        id='polar-spectrum',
        config={
            'displayModeBar': False
        }
    )
])

# Callback for updating the frequency spectrum plot
@app.callback(
    Output('frequency-spectrum', 'figure'),
    [Input('file-dropdown', 'value')]
)
def update_frequency_spectrum(file):
    df = pd.read_parquet(file)
    data = df['sample'].values
    freq, amps = get_envelope_spectrum(data)
    frequency_value = 236.4 # for BPFO Hz

    # Create the plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=freq[2:1000], y=amps[2:1000], mode='lines'))
    fig.add_shape(
        type='line',
        x0=frequency_value,
        x1=frequency_value,
        y0=0,
        y1=max(amps),
        line=dict(
            color='Red',
            dash='dash',
        )
    )
    fig.update_layout(
        title=f"Frequency Spectrum with BPFO at {frequency_value} Hz",
        xaxis_title="Frequency",
        yaxis_title="Amplitude",
        plot_bgcolor='#111111',
        paper_bgcolor='#111111',
        font_color='#7FDBFF',
    )
    return fig

# Callback for updating the polar spectrum plot
@app.callback(
    Output('polar-spectrum', 'figure'),
    Input('file-dropdown', 'value')
)
def update_polar_spectrum(file):
    df = pd.read_parquet(file)
    data = df['sample'].values
    _, amps = get_envelope_spectrum(data)
    fig = go.Figure()

    # Define a list of colors
    colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white', 'purple', 'orange']
    for i in range(len(amps[150:955])):
        # Calculate the (r, theta) coordinates of the points
        r_values = np.full(100, amps[150:955][i])  # 100 points with the same radius
        theta_values = np.linspace(0, 2*np.pi, 100)  # 100 points equally spaced over 360 degrees

        fig.add_trace(go.Scatterpolar(
            r = r_values,
            theta = theta_values * 180 / np.pi,  # Convert to degrees
            mode = 'lines',
            name = f'Amplitude {amps[i]:.2f}',
            line_color = colors[i % len(colors)],  # Use a different color for each line
        ))

    # Update the layout of the plot
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=False,
                showgrid=False,
                range=[0, max(amps)]
            ),
            angularaxis=dict(
                visible=False,
                showgrid=False
            )
        ),
        plot_bgcolor='#111111',
        paper_bgcolor='#111111',
        font_color='#7FDBFF',
        showlegend=False
    )

    return fig






if __name__ == '__main__':
    app.run_server(debug=True, port=8055)
