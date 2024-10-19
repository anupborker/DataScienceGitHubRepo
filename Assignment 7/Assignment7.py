import numpy as np

def create_3d_array(dim1, dim2, dim3):  # Function to create a 3D array based on given dimensions
    arr = np.zeros((dim1, dim2, dim3), dtype=int)

    for d1 in range(dim1):
        for d2 in range(dim2):
            for d3 in range(dim3):
                total = d1 + d2 + d3
                if (total % 10 == 2) or (total % 10 == 6):
                    arr[d1, d2, d3] = 0  # Assign 0 for certain index sums
                else:
                    arr[d1, d2, d3] = 1  # Assign 1 for other sums

    return arr

def find_longest_sequence(arr_3d):
    d1, d2, d3 = arr_3d.shape
    max_seq_len = 0
    start_pos = None
    seq_coords = []  # List to hold coordinates of the longest sequence

    for d1_idx in range(d1):
        for d2_idx in range(d2):
            current_length = 0
            temp_coords = []  # Temporarily hold coordinates for current sequence

            for d3_idx in range(d3):
                if arr_3d[d1_idx, d2_idx, d3_idx] == 1:
                    temp_coords.append((d1_idx, d2_idx, d3_idx))  # Add coordinate for 1
                    current_length += 1

                    if current_length > max_seq_len:
                        max_seq_len = current_length
                        start_pos = (d1_idx, d2_idx, d3_idx - current_length + 1)
                        seq_coords = temp_coords.copy()  # Update longest coordinates
                else:
                    current_length = 0
                    temp_coords = []  # Reset temporary coordinates if a 0 is found

    return max_seq_len, start_pos, seq_coords

# Define dimensions for the 3D matrix
x_size, y_size, z_size = 7, 5, 3
# Generate the 3D array
three_d_array = create_3d_array(x_size, y_size, z_size)

# Print the generated 3D array
for x in range(x_size):
    for y in range(y_size):
        for z in range(z_size):
            print(f"array[{x}][{y}][{z}] = {three_d_array[x][y][z]}")
        print()
    print()

# Call the function to find the longest sequence of 1s
longest_length, starting_position, longest_sequence_coords = find_longest_sequence(three_d_array)
print(f"Longest sequence of 1s length: {longest_length}")
print(f"Starting position of the longest sequence: {starting_position}")
print("Coordinates of the longest sequence:")
for coordinate in longest_sequence_coords:
    print(coordinate)
