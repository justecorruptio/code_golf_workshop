def spiral(mat):
    if not mat:
        return []
    return list(mat.pop(0)) + spiral(zip(*mat)[::-1])
