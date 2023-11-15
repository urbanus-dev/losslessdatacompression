import heapq
from collections import defaultdict

def huffman_encode(data):
    frequency = defaultdict(int)
    for symbol in data:
        frequency[symbol] += 1

    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# Example usage
original_data = "HELLO"
print("Original Data:", original_data)

encoded_data = huffman_encode(original_data)
print("Huffman Encoded Data:", encoded_data)
