def select(seq):
    n = len(seq)
    min_val =seq[0]
    for i in range(1, n):
        if seq[i] < min_val:
            min_val = seq[i]

    return min_val



if __name__ == '__main__':
    a = [ 5, 8, 2, 9,10, 7, 1]

    val = select(a)
    print(f'Minimum: {val}')
