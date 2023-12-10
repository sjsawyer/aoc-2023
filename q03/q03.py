def part1(grid):
    def get_neighbours(x, y):
        x_start = x
        x_end = x_start
        while x_end + 1 < len(grid[y]) and grid[y][x_end + 1].isdigit():
            x_end += 1

        for xx in range(x_start - 1, x_end + 2):
            for yy in range(y - 1, y + 2):
                if not 0 <= yy < len(grid) or not 0 <= xx < len(grid[yy]):
                    continue
                if yy == y and x_start <= xx <= x_end:
                    continue
                yield grid[yy][xx]

    def num_from_coord(x, y):
        x_start = x
        x_end = x_start
        while x_end + 1 < len(grid[y]) and grid[y][x_end + 1].isdigit():
            x_end += 1
        return int(grid[y][x_start : x_end + 1])

    # iterate over grid, when we find a number, check neighbours for symbol
    nums = []
    for y in range(len(grid)):
        is_new_number = True
        for x in range(len(grid[y])):
            c = grid[y][x]
            if c.isdigit() and is_new_number:
                # we have the beginning of a number
                is_new_number = False
                nbrs = get_neighbours(x, y)
                if any(cc for cc in nbrs if not cc == "." and not cc.isdigit()):
                    # append this number
                    nums.append(num_from_coord(x, y))
            elif not c.isdigit():
                is_new_number = True

    return sum(nums)


def part2(grid):
    def get_nbrs(x, y):
        nbrs = set()
        for xx in range(x - 1, x + 2):
            for yy in range(y - 1, y + 2):
                if xx == x and yy == y:
                    continue
                if not 0 <= xx < len(grid[0]):
                    continue
                if not 0 <= yy < len(grid):
                    continue
                nbrs.add((xx, yy))
        return nbrs

    def get_num(x, y):
        x_start, x_end = x, x
        coords = {(x, y)}
        while x_start - 1 >= 0 and grid[y][x_start - 1].isdigit():
            x_start -= 1
            coords.add((x_start, y))
        while x_end + 1 < len(grid[y]) and grid[y][x_end + 1].isdigit():
            x_end += 1
            coords.add((x_end, y))
        return int(grid[y][x_start : x_end + 1]), coords

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != "*":
                continue

            nbrs = get_nbrs(x, y)
            nums = []
            while nbrs:
                nx, ny = nbrs.pop()
                if grid[ny][nx].isdigit():
                    num, coords = get_num(nx, ny)
                    nbrs = nbrs.difference(coords)
                    nums.append(num)
            if len(nums) == 2:
                total += nums[0] * nums[1]

    return total


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    p1 = part1(data)
    print("Part 1:", p1)

    p2 = part2(data)
    print("Part 2:", p2)


main()
