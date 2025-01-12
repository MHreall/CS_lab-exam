import numpy as np

def compute_cross_product(array1, array2):
    if len(array1) != 3 or len(array2) != 3:
        raise ValueError("Both arrays must have exactly 3 elements.")
    
    return np.cross(array1, array2)

vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

cross_product = compute_cross_product(vector1, vector2)
print("Cross Product:", cross_product)  