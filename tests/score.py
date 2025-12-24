score = 0
results = []

def add(points, name):
    global score
    score += points
    results.append((name, points))
