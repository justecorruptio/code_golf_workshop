def rotate(mat):
    if not mat:
        return []

    w, h = len(mat[0]), len(mat)
    new = [[0] * h for i in xrange(w)]

    for y in xrange(h):
        for x in xrange(w):
            new[w - x - 1][y] = mat[y][x]
    return new

def spiral(mat):
    out = []
    while mat:
        out.extend(mat.pop(0))
        mat = rotate(mat)
    return out
