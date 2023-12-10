def part1(data):
    digits = set(str(i) for i in range(0, 10))

    sum = 0
    for line in data:
        line_digits = [c for c in line if c in digits]
        sum += int(line_digits[0] + line_digits[-1])

    return sum


DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    **{str(i): i for i in range(1, 10)},
}


def part2_slow(data):
    """Compare all slices."""

    sum = 0
    for line in data:
        nums_in_line = []
        for i in range(len(data)):
            for token in DIGITS:
                if line[i : i + len(token)] == token:
                    nums_in_line.append(token)
                    break
        sum += DIGITS[nums_in_line[0]] * 10 + DIGITS[nums_in_line[-1]]

    return sum


def part2_quick(data):
    """Substring search (via Trie)."""

    trie = {}

    def insert_into_trie(word, trie_):
        if not word:
            return

        c, *rest = word
        if c not in trie_:
            trie_[c] = {}
        insert_into_trie(rest, trie_[c])

    for word in DIGITS:
        insert_into_trie(word, trie)

    def substring(trie_, line, i, so_far):
        if not trie_:
            return so_far

        if i < len(line) and line[i] in trie_:
            so_far.append(line[i])
            return substring(trie_[line[i]], line, i + 1, so_far)

        return None

    sum = 0
    for line in data:
        nums_in_line = []
        for i in range(len(line)):
            res = substring(trie, line, i, [])
            if res is not None:
                nums_in_line.append(res)

        first, last = "".join(nums_in_line[0]), "".join(nums_in_line[-1])
        sum += DIGITS[first] * 10 + DIGITS[last]

    return sum


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    p1 = part1(data)
    print("Part 1:", p1)

    p2 = part2_quick(data)
    print("Part 2:", p2)


main()
