def part1(games):
    total = 0
    for winners, chosen in games:
        n_match = len(chosen.intersection(winners))
        if n_match:
            total += 1 << (len(chosen.intersection(winners)) - 1)
    return total


def part2(games):
    freq = {i: 1 for i in range(len(games))}
    for i, (winners, chosen) in enumerate(games):
        n_match = len(chosen.intersection(winners))
        if n_match:
            for j in range(i + 1, i + n_match + 1):
                freq[j] += freq[i]

    return sum(freq.values())


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()
        games = []
        for line in data:
            _, rest = line.split(":")
            winners, chosen = rest.split("|")
            winners = set(winners.strip().split())
            chosen = set(chosen.strip().split())
            games.append((winners, chosen))

    p1 = part1(games)
    print("Part 1:", p1)

    p2 = part2(games)
    print("Part 2:", p2)


main()
