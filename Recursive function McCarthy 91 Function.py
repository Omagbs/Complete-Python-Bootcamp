#McCarthy 91 Function using recursive function

def M(n):
    if n > 100:
       return n - 10
    else:
        return M(M(n+11))

print(M(102))