def  chickens(p, q, r, m):
    time = 0
    hens = 1
    chickens = []
    eggs = [(p, 0)]
    while (time <= m):
        chickens = filter(None, [(noChick, months+1) if (months < q) else hens+=noChick  for (noChick, months) in eggs])
        eggs = filter(None, [(noEggs, months+1) if (months < q) else chickens.append((noEggs, 0)) for (noEggs, months) in eggs])
        eggs.append((hens*p, 0))

        print eggs
        print chickens
        time += 1
        
chickens(2, 1, 1, 8)
        
