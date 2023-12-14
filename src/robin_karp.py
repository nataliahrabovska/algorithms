def rabin_karp(haystack, needle):
    length_needle = len(needle)
    length_haystack = len(haystack)
    skip = 0
    res = []

    table_of_displacements = [-1] * 256
    for index_haystack in range(length_needle):
        table_of_displacements[ord(needle[index_haystack])] = index_haystack

    index_needle = 0
    while index_needle <= length_haystack - length_needle:
        skip = 0
        for index_haystack in range(length_needle - 1, -1, -1):
            if needle[index_haystack] != haystack[index_needle + index_haystack]:
                skip = max(1, index_haystack - table_of_displacements[ord(haystack[index_needle + index_haystack])])
                break

        if skip == 0:
            res.append(index_needle)
            skip = 1

        index_needle += skip

    return res
