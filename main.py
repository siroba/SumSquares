#!/bin/python

def get_nth(X, Y, i=0, count=0):
    if i >= len(Y) or count > X:
        return ''

    if Y[i] == ' ':
        count += 1

    if count == X:
        return Y[i] + get_nth(X, Y, i=i + 1, count=count)

    return get_nth(X, Y, i=i + 1, count=count)


def solve(X, Y):
    if X == 0:
        return 0

    _Y = int(get_nth(X - 1, Y))

    result = 0
    ot = solve(X - 1, Y)

    if _Y > 0:
        result += _Y ** 2

    return result + ot


def get_input(N=0):
    if N == 0:
        return

    X = int(input())
    Y = input()

    recursive_res = get_input(N - 1)
    my_res = solve(X, Y)

    if recursive_res:
        print("%d\n%d" % (recursive_res, my_res))
    else:
        print(my_res)


def main():
    N = int(input())

    get_input(N)


if __name__ == '__main__':
    main()
