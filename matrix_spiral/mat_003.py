def spiral(mat):
    out = []
    while mat:
        out.extend(mat.pop(0))
        mat = zip(*mat)[::-1]
    return out
