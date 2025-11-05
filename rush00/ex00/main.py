from checkmate import checkmate

def main():
    # การวางตำแหน่งของตัวหมากรุกบนกระดาน
    board = """\
R.K.
....
....
....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()
