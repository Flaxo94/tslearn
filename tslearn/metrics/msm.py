import numpy as np

def C(new_point, x, y, c):
    
    if (x <= new_point and new_point <= y) or (y <= new_point and new_point <= x):
        dist = c
    else:
        dist = c + min(np.abs(new_point-x), np.abs(new_point-y))
    
    return dist

def msm(dataset1, dataset2, **kwargs):
    
    try:
        c = kwargs["c"]
    except KeyError:
        c = 0.1
    
    #if not isinstance(dataset1, np.ndarray):
    dataset1 = np.array(dataset1)
    #if not isinstance(dataset1, np.ndarray):
    dataset2 = np.array(dataset2)

    m = dataset1.size
    n = dataset2.size
    
    Cost = np.zeros((m, n))

    Cost[0, 0] = np.abs(dataset1[0] - dataset2[0]).item(0)

    # Initialization
    for i in range(1, m):
        Cost[i, 0] = Cost[i-1, 0] + C(dataset1[i], dataset1[i-1], dataset2[0], c)

    for i in range(1, n):
        Cost[0, i] = Cost[0, i-1] + C(dataset2[i], dataset1[0], dataset2[i-1], c)

    return 5

    # Main loop
    for i in range(1, m):
        for j in range(1, n):
            d1 = Cost[i-1, j-1] + np.abs(dataset1[i] - dataset2[j])
            d2 = Cost[i-1, j] + C(dataset1[i], dataset1[i-1], dataset2[j], c)
            d3 = Cost[i, j-1] + C(dataset2[j], dataset1[i], dataset2[j-1], c)
            Cost[i, j] = min(d1, d2, d3)
    
    #print(Cost)
    distance = Cost[m-1, n-1]
    return distance