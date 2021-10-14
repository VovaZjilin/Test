p = [
    (  0,  0),
    (100,100),
    (200,100),
    (100,200),
]

for A, B in [p[i:i+2] for i in range(len(p)-1)]:
    x0, y0 = A
    x1, y1 = B 
    g = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    print(g)
    g0 = 0
    t = 1
    v = 10
    while g0 < g:
        g0 += v * t
        print(g, g0)

    
    
    
    
