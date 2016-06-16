s = lambda m: list(m.pop(0)) + s(zip(*m)[::-1]) if m else []
