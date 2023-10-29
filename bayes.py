# Define the dataset
dataset = [[0, 0, 1, 0, 0], [0, 0, 1, 1, 0], [1, 0, 1, 0, 1], [2, 1, 1, 0, 1], [2, 2, 0, 0, 1],
           [2, 2, 0, 1, 0], [1, 2, 0, 1, 1], [0, 1, 1, 0, 0], [0, 2, 0, 0, 1], [2, 1, 0, 0, 1],
           [0, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [2, 1, 1, 1, 0]]

# Separate the data into classes
mp = {0: [], 1: []}
for row in dataset:
    mp[row[-1]].append(row)

# Define the test input
test = [2, 1, 1, 1]

# Calculate probability for class 'Yes' and class 'No'
py, pn = len(mp[1]) / len(dataset), len(mp[0]) / len(dataset)

# Calculate conditional probabilities for each feature
for i in range(len(test)):
    py *= len([row for row in mp[1] if row[i] == t[i]]) / len(mp[1])
    pn *= len([row for row in mp[0] if row[i] == t[i]]) / len(mp[0])

# Calculate the final probability
prob = py / (py + pn)

# Print the result
print(f"Probability of playing golf: {prob * 100:.2f}%")
