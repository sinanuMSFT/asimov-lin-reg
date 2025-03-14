import numpy as np

# Laptop dataset: Each row is a laptop, each column is a feature

# Processor Speed (GHz)
# Hard Drive Size (GB)
# Weight (kg)
# Memory (GB)
# Processor Generation

X = np.array([
    [2.5, 512, 1.8, 8, 2],   # Laptop 1
    [3.2, 1024, 2.2, 16, 3], # Laptop 2
    [1.8, 256, 1.5, 4, 1]     # Laptop 3
])

# Actual laptop prices
y = np.array([1200, 2200, 800])  # Market prices in dollars

# Possible coefficient values to evaluate
candidates = np.array([
    [10, 0.1, -5, 20, 50],  # Coefficient set 1
    [50, 0.2, -10, 50, 100],  # Coefficient set 2
    [100, 0.3, -20, 100, 150],  # Coefficient set 3
    [250, 0.4, -80, 150, 250],   # Coefficient set 4
    [400, 0.8, -150, 200, 350]   # Coefficient set 5
])

def squared_error(X, y, c):
    """Computes the sum of squared errors (SSE) for a given coefficient set."""
    predictions = X @ c  # Matrix multiplication to get price estimates
    print(f"Predictions: {predictions}")
    errors = (y - predictions) ** 2  # Squared differences
    return np.sum(errors)  # Total error

# Find the best coefficient set
best_index = None
best_error = float('inf')

for i, c in enumerate(candidates):
    error = squared_error(X, y, c)
    print(f"Set {i+1}: Squared Error = {error:>15,.2f}\n")
    
    if error < best_error:
        best_error = error
        best_index = i

print(f"\nBest coefficient set: Set {best_index+1} with SSE = {best_error:>15,.2f}")