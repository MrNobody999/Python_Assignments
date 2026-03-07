import math

Border = "-"*40

# Dataset
dataset = [
    {"point": "A", "x": 1, "y": 2, "label": "Red"},
    {"point": "B", "x": 2, "y": 3, "label": "Red"},
    {"point": "C", "x": 3, "y": 1, "label": "Blue"},
    {"point": "D", "x": 6, "y": 5, "label": "Blue"},
]

K = 3

# Step 1 : Accept input from user
print(Border)
print("Step 1 : Accept input from user")
print(Border)

new_x = float(input("Enter X coordinate: "))
new_y = float(input("Enter Y coordinate: "))

print(f"New point coordinates : ({new_x}, {new_y})")

# Step 2 : Calculate Euclidean distance
print(Border)
print("Step 2 : Calculate Euclidean distance")
print(Border)

# Euclidean Distance Formula:
# d = sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )

distances = []

for data in dataset:
    dist = math.sqrt((new_x - data["x"])**2 + (new_y - data["y"])**2)
    distances.append({"point": data["point"], "label": data["label"], "distance": dist})
    print(f"Distance from {data['point']} ({data['x']},{data['y']}) : {round(dist, 2)}")

# Step 3 : Sort distances
print(Border)
print("Step 3 : Sort distances")
print(Border)

distances.sort(key=lambda d: d["distance"])

print("Sorted distances (nearest to farthest) :")
for d in distances:
    print(f"  {d['point']} - Distance: {round(d['distance'], 2)}  Label: {d['label']}")

# Step 4 : Select K nearest neighbors
print(Border)
print("Step 4 : Select K nearest neighbors")
print(Border)

k_neighbors = distances[:K]

print(f"K = {K} nearest neighbors selected :")
for neighbor in k_neighbors:
    print(f"  {neighbor['point']} - Distance: {round(neighbor['distance'], 2)}  Label: {neighbor['label']}")

# Step 5 : Predict class using majority voting
print(Border)
print("Step 5 : Predict class using majority voting")
print(Border)

vote_count = {}

for neighbor in k_neighbors:
    label = neighbor["label"]
    if label not in vote_count:
        vote_count[label] = 0
    vote_count[label] += 1

print("Vote count :", vote_count)

predicted_class = max(vote_count, key=vote_count.get)

# Output
print(Border)
print("Final Output")
print(Border)

print("Nearest Neighbors:")
for neighbor in k_neighbors:
    print(f"  {neighbor['point']} - Distance: {round(neighbor['distance'], 2)}")

print(f"\nPredicted Class: {predicted_class}")
print(Border)
