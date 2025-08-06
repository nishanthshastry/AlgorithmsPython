import math

def closest_pair(points):
    # Sort the input points by x-coordinate
    px = sorted(points, key=lambda p: p[0])
    # Sort the input points by y-coordinate
    py = sorted(points, key=lambda p: p[1])
    # Start the recursive closest pair search using sorted lists
    # Returns only the pair of points (the [1] selects the second item from the tuple)
    # return closest_pair_rec(px, py)[1]
    d, best_pair = closest_pair_rec(px, py)
    return d, best_pair

def distance(p1, p2):
    # Compute the Euclidean distance between two points p1 and p2
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

def brute_force(points):
    # This function checks all possible pairs (brute force) and returns the closest one
    min_dist = float('inf')  # Start with infinity as the minimum distance
    pair = None              # Store the closest pair found
    n = len(points)
    # Check every possible pair of points
    for i in range(n):
        for j in range(i+1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return min_dist, pair  # Return the closest pair and their distance

def closest_pair_rec(px, py):
    # Recursive function to find the closest pair using divide and conquer
    n = len(px)
    if n <= 3:
        # If 3 or fewer points, use brute-force directly
        return brute_force(px)

    # Find the middle index for dividing the set
    mid = n // 2
    # Divide points sorted by x into left (Qx) and right (Rx) halves
    Qx = px[:mid]
    Rx = px[mid:]
    # x-coordinate of the dividing vertical line
    mid_x = px[mid][0]

    # Divide points sorted by y into left (Qy) and right (Ry) by their x-coordinates
    Qy = [p for p in py if p[0] <= mid_x]
    Ry = [p for p in py if p[0] > mid_x]

    # Recursively find closest pairs in left and right halves
    (dL, pairL) = closest_pair_rec(Qx, Qy)
    (dR, pairR) = closest_pair_rec(Rx, Ry)

    # Determine which pair is closer: left or right
    if dL < dR:
        d = dL
        best_pair = pairL
    else:
        d = dR
        best_pair = pairR

    # Build a strip of points that are within distance d of the dividing line
    # Only these could possibly form a closer pair crossing the divide
    Sy = [p for p in py if abs(p[0] - mid_x) < d]

    # Check the strip: for each point, check only the next 7 points in y-sorted order
    # (CLRS and geometry show that no need to check more than 7 ahead)
    for i in range(len(Sy)):
        for j in range(i+1, min(i+8, len(Sy))):
            p, q = Sy[i], Sy[j]
            dst = distance(p, q)
            # If a closer pair is found in the strip, update d and best_pair
            if dst < d:
                d = dst
                best_pair = (p, q)
    # Return the closest distance and pair found in this recursive call
    return d, best_pair
