l,d,v,g,r = map(int, input().split())
time = d/v
if time<g:
    print(l/v)
elif time == g:
    print(d/v + r-(d/v-g) + (l-d)/v)
else:
    time = d/v
    c = time%(g+r)
    if c == 0 or c<g:
        print(l/v)
    else:
        print(d/v+r-(time%(g+r)-g)+(l-d)/v)

        
