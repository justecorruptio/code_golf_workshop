#s = lambda m: list(m.pop(0)) + s(zip(*m)[::-1]) if m else []
#s=lambda m:list(m.pop(0))+s(zip(*m)[::-1])if m else[]
#s=lambda m:m and list(m.pop(0))+s(zip(*m)[::-1])or[]
s=lambda m:m and list(m[0])+s(zip(*m[1:])[::-1])or[]
