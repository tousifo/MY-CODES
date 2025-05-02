def min_puzzle_diff(n, pieces):
    pieces.sort()
    best = float('inf')
    for i in range(len(pieces) - n + 1):
        diff = pieces[i + n - 1] - pieces[i]
        if diff < best:
            best = diff
    return best

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    n, m = map(int, data[:2])
    pieces = list(map(int, data[2:2 + m]))
    print(min_puzzle_diff(n, pieces))
