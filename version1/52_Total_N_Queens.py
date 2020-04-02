global num


def solve_n_queens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    global num
    num = 0
    solve([], n)
    print num


def solve(previous, n):
    if len(previous) == n:
        global num
        num += 1
        return
    else:
        r = len(previous)
        for j in range(n):
            if r == 0:
                previous.append(j)
                solve(previous, n)
                previous.pop()
            else:
                valid = True
                for k in range(r):
                    # used coors : coor = [k, previous[k]]
                    if j == previous[k] or (j - r == previous[k] - k) or (j + r == previous[k] + k):
                        valid = False
                        break
                if valid:
                    previous.append(j)
                    solve(previous, n)
                    previous.pop()


print solve_n_queens(4)
