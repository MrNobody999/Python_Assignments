import math

Border = "-"*40

# Dataset
dataset = [
    {"point": "A", "x": 1, "y": 2, "label": "Red"},
    {"point": "B", "x": 2, "y": 3, "label": "Red"},
    {"point": "C", "x": 3, "y": 1, "label": "Blue"},
    {"point": "D", "x": 6, "y": 5, "label": "Blue"},
]

K_values = [1, 3, 5]

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
# d = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

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

# Step 4 : Predict class for each value of K

print(Border)
print("Step 4 : Predict class for each value of K")
print(Border)

results = {}

for K in K_values:

    print(f"\n--- K = {K} ---")

    # Select K nearest neighbors
    # If K > total dataset points, use all available points
    k_neighbors = distances[:min(K, len(distances))]

    print(f"Selected {len(k_neighbors)} neighbor(s) :")
    for neighbor in k_neighbors:
        print(f"  {neighbor['point']} - Distance: {round(neighbor['distance'], 2)}  Label: {neighbor['label']}")

    # Majority voting
    vote_count = {}
    for neighbor in k_neighbors:
        label = neighbor["label"]
        if label not in vote_count:
            vote_count[label] = 0
        vote_count[label] += 1

    print(f"Vote count : {vote_count}")

    predicted_class = max(vote_count, key=vote_count.get)
    results[K] = predicted_class

    print(f"Predicted Class for K={K} : {predicted_class}")

# Step 5 : Display prediction results summary

print(Border)
print("Step 5 : Display prediction results summary")
print(Border)

print("Prediction Results:")
for K, pred in results.items():
    print(f"  K = {K} -> {pred}")

# Step 6 : Explain why prediction changes with K

print(Border)
print("Step 6 : Explain why prediction changes with K")
print(Border)

explanation = """
Why does the prediction change when K increases?

K = 1  :
  - Only the single nearest neighbor is considered.
  - The closest point to (2,2) is A(1,2) or B(2,3) which are both Red.
  - So prediction = Red  (influenced by just 1 point)

K = 3  :
  - The 3 nearest neighbors are considered : A, B, C
  - Red votes = 2 (A, B)  |  Blue votes = 1 (C)
  - Majority = Red
  - So prediction = Red

K = 5 
  - All 4 available points are considered : A, B, C, D
  - Since dataset has only 4 points, K=5 uses all 4.
  - Red votes = 2 (A, B)  |  Blue votes = 2 (C, D)
  - In case of a tie, max() picks the first max found = Blue
  - So prediction = Blue

"""

print(explanation)
print(Border)