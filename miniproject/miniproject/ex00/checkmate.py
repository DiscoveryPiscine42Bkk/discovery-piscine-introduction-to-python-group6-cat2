def checkmate(board_str: str):
                

        rows = [r.rstrip() for r in board_str.strip().split("\n") if r.strip()]
        board = [list(r) for r in rows]
        n = len(board)

        if not all(len(row) == n for row in board):
            print("Error")
            return


        king_pos = None
        for i in range(n):
            for j in range(n):
                if board[i][j] == "K":
                    king_pos = (i, j)
                    break
            if king_pos:
                break

        if not king_pos:
            print("Error")
            return

        kx, ky = king_pos

        def in_bounds(x, y):
            return 0 <= x < n and 0 <= y < n


        pawn_dirs = [(1, -1), (1, 1)]
        for dx, dy in pawn_dirs:
            x, y = kx + dx, ky + dy
            if in_bounds(x, y) and board[x][y] == "P":
                print("Success")
                return

 
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            x, y = kx + dx, ky + dy
            while in_bounds(x, y):
                cell = board[x][y]
                if cell != ".":
                    if cell in ("B", "Q"):
                        print("Success")
                        return
                    break
                x += dx
                y += dy


        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = kx + dx, ky + dy
            while in_bounds(x, y):
                cell = board[x][y]
                if cell != ".":
                    if cell in ("R", "Q"):
                        print("Success")
                        return
                    break
                x += dx
                y += dy


        knight_moves = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]
        for dx, dy in knight_moves:
            x, y = kx + dx, ky + dy
            if in_bounds(x, y) and board[x][y] == "N":

                print("Success")
                return
             

            
            print("Fail")