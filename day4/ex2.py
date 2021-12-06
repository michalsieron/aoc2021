def mark(board, n):
    for i, row in enumerate(board):
        board[i] = [
            0 if v == n else v
            for v in row
        ]


def is_winning(board):
    rows = any(r.count(0) == 5 for r in board)
    cols = any(c.count(0) == 5 for c in zip(*board))
    return rows or cols


def score(board, n):
    return int(n) * sum(
        sum(map(int, row)) for row in board
    )


def play(boards, rand):
    for r in rand:
        for b in boards.copy():
            mark(b, r)
            if is_winning(b):
                boards.remove(b)
                if len(boards) == 0:
                    return score(b, r)


with open("test_data.txt", "r") as fd:
    rand = fd.readlines(2)[0].strip().split(",")
    boards = [
        [l.split() for l in board.splitlines()]
        for board in fd.read().split("\n\n")
    ]

print("answer:", play(boards, rand))
