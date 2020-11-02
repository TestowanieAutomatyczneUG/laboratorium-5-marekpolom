def distance(dist_1, dist_2):
    j = 0

    for i in range(0, len(dist_1)):
        if dist_1[i] != dist_2[i]:
            j+=1

    return j