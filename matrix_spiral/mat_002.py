def rotate(mat):
    return zip(*mat)[::-1]

def spiral(mat):
    out = []
    while mat:
        out.extend(mat.pop(0))
        mat = rotate(mat)
    return out
