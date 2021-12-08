def length_of_longest_substring(s: str) -> int:
    character_set = set()
    pointer_a = 0
    pointer_b = 0
    length_of_longest = 0
    while pointer_b < len(s):
        while s[pointer_b] in character_set:
            character_set.remove(s[pointer_a])
            pointer_a += 1
        character_set.add(s[pointer_b])
        pointer_b += 1
        length_of_longest = max(length_of_longest, len(character_set))

    return length_of_longest
