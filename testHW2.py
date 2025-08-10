def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    #your code here

    def next_pos(row , col):
        col += 1
        if col >= len(words[row]):
            row += 1
            col = 0
        return row , col
        
    max_len = 0
    sequences = []

    total_len = sum(len(row) for row in words)

    pos_list =  []
    r, c = 0, 0
    for _ in range(total_len):
        pos_list.append((r, c))
        r, c = next_pos(r, c)

    for stat_r, stat_c in pos_list:
        seen = set()
        currnt_seq = []
        r, c = stat_r, stat_c

        while r < len(words):
            word = words[r][c]
            if word in seen:
                break
            seen.add(word)
            currnt_seq.append(word)
            r, c = next_pos(r, c)

        if len(currnt_seq) > max_len:
            max_len = len(currnt_seq)
            sequences = [currnt_seq]
        elif len(currnt_seq) == max_len:
            sequences.append(currnt_seq)

    return max_len, sequences

words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])

words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])
