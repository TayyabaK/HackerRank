def root(x):
    if par[x]==-1:
        return x
    par[x] = root(par[x])
    return par[x]

def unite(x,y):
    x = root(x)
    y = root(y)
    if x == y :
        return
    if x < y:
        x,y = y,x
    sz[x] += sz[y]
    par[y] = x

for t in xrange(input()):
    n,m = map( int, raw_input().split() )
    par = [-1]*(n+1)
    sz = [1]*(n+1)
    
    for i in xrange(m):
        xx,yy = map( int, raw_input().split() )
        unite( xx, yy )
    
    ar = []
    vis = [0]*(n+1)
    for i in xrange(1,n+1):
        x = root(i)
        if vis[x] == 0 :
            vis[x] = 1
            ar.append(sz[x])
    
    ar = sorted(ar)[::-1]
    
    ans = 0
    for v in ar :
        ans += ( v*v*v - v )/3
        m -= v
        m += 1
        ans += m*v*(v-1)
    
    print ans
