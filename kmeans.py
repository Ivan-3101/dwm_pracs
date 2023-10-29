import math

# Points
points = [(2, 3), (2, 4), (8, 9), (7, 8), (1, 2), (8, 8), (9, 7), (2, 2)]

# Initial means (select randomly)
m1, m2 = (2, 3), (2, 4)

iteration = 0

while True:
    iteration += 1
    
    print(f"\nIteration {iteration}")
    
    # Storing the values as old means to check if clusters change
    om1, om2 = m1, m2
    
    k1 = [point for point in points if math.dist(point, m1) < math.dist(point, m2)]
    k2 = [point for point in points if math.dist(point, m1) >= math.dist(point, m2)]
    
    # Show the clusters formed
    print(f"Cluster 1: {k1}")
    print(f"Cluster 2: {k2}")
    
    # Calculate means from the clusters formed
    m1 = (sum(p[0] for p in k1) / len(k1), sum(p[1] for p in k1) / len(k1))
    m2 = (sum(p[0] for p in k2) / len(k2), sum(p[1] for p in k2) / len(k2))
    
    # Printing the means calculated
    print(f"m1: {m1}\nm2: {m2}")
    
    # Checking if any changes took place in this iteration
    if m1 == om1 and m2 == om2:
        # Clusters remained the same in this iteration
        break

print(f"\nFinal Clusters Created\nCluster 1: {k1}\nCluster 2: {k2}")
