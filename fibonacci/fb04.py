import plotly.graph_objects as go
import numpy as np

def generate_fibonacci_3d(n):
    # Generate Fibonacci sequence
    fib = [1, 1]  # Starting with first two numbers
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    # Create 3D coordinates (using same number for x, y, z)
    coordinates = [[x, x, x] for x in fib]
    coords = np.array(coordinates)
    
    # Extract x, y, z coordinates
    x = coords[:, 0]
    y = coords[:, 1]
    z = coords[:, 2]
    
    return x, y, z

# Get user input
try:
    sequence_length = int(input("Enter the desired length of Fibonacci sequence (minimum 2): "))
    if sequence_length < 2:
        print("Length must be at least 2. Using default value of 9.")
        sequence_length = 9
except ValueError:
    print("Invalid input. Using default value of 9.")
    sequence_length = 9

# Generate coordinates
x, y, z = generate_fibonacci_3d(sequence_length)

# Create the 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers+lines',
    marker=dict(
        size=5,
        color='red',
    ),
    line=dict(
        color='blue',
        width=2
    ),
    text=[f'({xi}, {yi}, {zi})' for xi, yi, zi in zip(x, y, z)],
    hoverinfo='text'
)])

# Update layout
fig.update_layout(
    title=f'3D Fibonacci Sequence (Length: {sequence_length})',
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis',
        aspectmode='cube'
    ),
    showlegend=False
)

# Show the plot
fig.show()