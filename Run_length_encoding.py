def run_length_encode(data):
    encoded_data = []
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded_data.append((data[i - 1], count))
            count = 1

    encoded_data.append((data[-1], count))
    return encoded_data

def run_length_decode(encoded_data):
    decoded_data = []

    for item in encoded_data:
        decoded_data.extend([item[0]] * item[1])

    return decoded_data

# Example usage
original_data = [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5]
print("Original Data:", original_data)

encoded_data = run_length_encode(original_data)
print("Encoded Data:", encoded_data)

decoded_data = run_length_decode(encoded_data)
print("Decoded Data:", decoded_data)
