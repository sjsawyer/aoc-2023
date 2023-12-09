import functools


def part1(games):
    amounts = {"red": 12, "green": 13, "blue": 14}
    total = 0
    for i, game in enumerate(games, start=1):
        possible = True
        for turn in game:
            for color in amounts:
                if turn.get(color, 0) > amounts[color]:
                    possible = False
        if possible:
            total += i
    return total


def part2(games):
    colors = ("red", "green", "blue")
    total = 0
    for game in games:
        total += functools.reduce(
            lambda x, y: x * y,
            (max(round_.get(color, 0) for round_ in game) for color in colors),
        )

    return total


def main():
    games = []
    with open("input.txt") as f:
        for line in f:
            game = []
            rounds = line.split(":")[-1].split(";")
            for round_ in rounds:
                r = {}
                turns = round_.split(",")
                for turn in turns:
                    n, color = turn.strip().split(" ")
                    r[color] = int(n)
                game.append(r)
            games.append(game)

    p1 = part1(games)
    print("Part 1:", p1)

    p2 = part2(games)
    print("Part 2:", p2)


main()
