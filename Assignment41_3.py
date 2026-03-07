import math

Border = "-"*40

# Dataset
dataset = [
    {"student": "S1", "study_hours": 2, "attendance": 60, "result": "Fail"},
    {"student": "S2", "study_hours": 5, "attendance": 80, "result": "Pass"},
    {"student": "S3", "study_hours": 6, "attendance": 85, "result": "Pass"},
    {"student": "S4", "study_hours": 1, "attendance": 50, "result": "Fail"},
]

K = 3

# Step 1 : Accept input from user
print(Border)
print("Step 1 : Accept input from user")
print(Border)

study_hours = float(input("Enter Study Hours : "))
attendance  = float(input("Enter Attendance  : "))

print(f"New student data : Study Hours = {study_hours}, Attendance = {attendance}")

# Step 2 : Calculate Euclidean distance
print(Border)
print("Step 2 : Calculate Euclidean distance")
print(Border)

# Euclidean Distance Formula :
# d = sqrt( (sh2 - sh1)**2 + (att2 - att1)**2 )

distances = []

for data in dataset:
    dist = math.sqrt(
        (study_hours - data["study_hours"])**2 +
        (attendance  - data["attendance"])**2
    )
    distances.append({
        "student"     : data["student"],
        "study_hours" : data["study_hours"],
        "attendance"  : data["attendance"],
        "result"      : data["result"],
        "distance"    : dist
    })
    print(f"Distance from {data['student']} "
          f"(Hours={data['study_hours']}, Att={data['attendance']}, {data['result']}) "
          f": {round(dist, 2)}")

# Step 3 : Sort distances
print(Border)
print("Step 3 : Sort distances")
print(Border)

distances.sort(key=lambda d: d["distance"])

print("Sorted distances (nearest to farthest) :")
for d in distances:
    print(f"  {d['student']} - Distance: {round(d['distance'], 2)}  Result: {d['result']}")

# Step 4 : Select K nearest neighbors
print(Border)
print("Step 4 : Select K nearest neighbors")
print(Border)

k_neighbors = distances[:K]

print(f"K = {K} nearest neighbors selected :")
for neighbor in k_neighbors:
    print(f"  {neighbor['student']} - "
          f"Hours: {neighbor['study_hours']}, "
          f"Attendance: {neighbor['attendance']}, "
          f"Distance: {round(neighbor['distance'], 2)}, "
          f"Result: {neighbor['result']}")

# Step 5 : Majority voting
print(Border)
print("Step 5 : Majority voting")
print(Border)

vote_count = {}

for neighbor in k_neighbors:
    label = neighbor["result"]
    if label not in vote_count:
        vote_count[label] = 0
    vote_count[label] += 1

print("Vote count :", vote_count)

predicted_result = max(vote_count, key=vote_count.get)

# Final Output
print(Border)
print("Final Output")
print(Border)

print("Nearest Neighbors :")
for neighbor in k_neighbors:
    print(f"  {neighbor['student']} - Distance: {round(neighbor['distance'], 2)}  Result: {neighbor['result']}")

print(f"\nPredicted Result: {predicted_result}")
print(Border)