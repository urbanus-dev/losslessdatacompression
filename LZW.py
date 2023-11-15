# LZW
def lzw_encode(data):
    dictionary = {chr(i): i for i in range(256)}
    result = []
    current_code = 256
    current_sequence = data[0]

    for symbol in data[1:]:
        current_sequence += symbol
        if current_sequence not in dictionary:
            result.append(dictionary[current_sequence[:-1]])
            dictionary[current_sequence] = current_code
            current_code += 1
            current_sequence = symbol

    result.append(dictionary[current_sequence])
    return result
def lzw_decode(encoded_data):
    dictionary = {i: chr(i) for i in range(256)}
    result = []
    current_code = 256
    old_symbol = chr(encoded_data.pop(0))
    result.append(old_symbol)

    for code in encoded_data:
        if code not in dictionary:
            new_symbol = old_symbol + old_symbol[0]
        else:
            new_symbol = dictionary[code]

        result.append(new_symbol)
        dictionary[current_code] = old_symbol + new_symbol[0]
        current_code += 1
        old_symbol = new_symbol

    return result
# Example usage
original_data = "HELLOO"
print("Original Data:", original_data)
encode_data=lzw_encode(original_data)
print("Encoded Data:", encode_data)
decode_data=lzw_decode(encode_data)
print("Decoded Data:", decode_data)


