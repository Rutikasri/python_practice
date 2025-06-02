def game(n,m):
    return((n+1)//2)*((m+1)//2)
n,m = map (int, input().split())
print(game(n,m))