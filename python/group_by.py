from itertools import groupby

data = [
    {"name": 1, "department": "a"},
    {"name": 2, "department": "b"},
    {"name": 3, "department": "a"},
    {"name": 4, "department": "c"},
    {"name": 5, "department": "b"}
]

# Sort the data based on the "department" attribute
data.sort(key=lambda x: x["department"])

# Group the sorted data by the "department" attribute
grouped_data = [list(group) for _, group in groupby(data, key=lambda x: x["department"])]

# Print the output
for group in grouped_data:
    print(group)
