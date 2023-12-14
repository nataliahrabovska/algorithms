def rabin_karp(haystack: str, needle: str) -> list:
    if not haystack or not needle:
        return []

    length_needle = len(needle)
    length_haystack = len(haystack)
    found_positions = []

    base = 256
    prime = 101

    def calculate_hash(string: str, length: int) -> int:

        hash_value = 0
        for i in range(length):
            hash_value = (hash_value * base + ord(string[i])) % prime
        return hash_value

    needle_hash = calculate_hash(needle, length_needle)
    haystack_hash = calculate_hash(haystack, length_needle)

    for start in range(length_haystack - length_needle + 1):
        if needle_hash == haystack_hash and haystack[start:start + length_needle] == needle:
            found_positions.append(start)

        if start < length_haystack - length_needle:
            haystack_hash = (base * (haystack_hash - ord(haystack[start]) * pow(base, length_needle - 1, prime)) +
                             ord(haystack[start + length_needle])) % prime

    return found_positions
