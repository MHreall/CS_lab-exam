import numpy as np

def reconstruct_matrix(U, S, V):
    if len(S.shape) == 1:
        S = np.diag(S)
    
    reconstructed_matrix = np.dot(U, np.dot(S, V))
    return reconstructed_matrix

U = np.array([[0.58, 0.58, 0.58], [0.58, -0.81, 0.0], [0.58, 0.0, -0.81]])
S = np.array([3, 2, 1])
V = np.array([[0.58, 0.58, 0.58], [0.58, -0.81, 0.0], [0.58, 0.0, -0.81]])

original_matrix = reconstruct_matrix(U, S, V)
print("Reconstructed Matrix:")
print(original_matrix)
