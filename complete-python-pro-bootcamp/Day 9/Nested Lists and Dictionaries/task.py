capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
for name in capitals:
    print(name)

# Nested lists

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# Print Lille

# print(travel_log["France"][1])

# nested list

nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])


travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 8
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

print(travel_log["Germany"]["cities_visited"][2])
