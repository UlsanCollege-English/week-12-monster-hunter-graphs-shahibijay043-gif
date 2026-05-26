[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/80z-ZS6n)
# Week 12: Monster Hunter Graphs

Student

Name: Shahi Bijay

Student ID: 2412083

Summary

This assignment focused on building and analyzing monster hunting graphs using Python. I created both weighted and unweighted undirected graphs to represent monster hunting locations and routes between them. Each location represents a monster sighting area, while each route represents a travel connection between locations. I also implemented graph analysis functions such as finding the most connected location and organizing hunting reports using a heap priority queue. The hardest function for me was build_weighted_hunter_map because it required handling duplicate routes and validating danger scores correctly.

Approach
build_hunter_map:
Used a dictionary with sets to avoid duplicate neighbors.
Added routes in both directions for an undirected graph.
Converted sets into sorted lists before returning.
build_weighted_hunter_map:
Used nested dictionaries to store weighted routes.
Added both directions for every route.
Kept the smallest danger score for duplicate routes.
Raised ValueError for invalid weights.
map_summary:
Counted total locations using len(graph).
Counted unique undirected routes using sets.
most_connected_location:
Compared neighbor counts for each location.
Returned the alphabetically first location during ties.
priority_hunt_order:
Used Python’s heapq module as a priority queue.
Returned locations ordered from most urgent to least urgent.
Complexity
build_hunter_map
Time:
O(E log V)
Space:
O(V + E)
Why:
Each route is processed once, and sorting neighbors adds extra logarithmic cost.
build_weighted_hunter_map
Time:
O(E log V)
Space:
O(V + E)
Why:
Every weighted route is inserted into the graph, and sorting dictionary items increases runtime slightly.
map_summary
Time:
O(V + E)
Space:
O(E)
Why:
The function checks every location and every route once while storing unique routes in a set.
most_connected_location
Time:
O(V)
Space:
O(1)
Why:
The function scans all locations once and only stores a few variables.
priority_hunt_order
Time:
O(N log N)
Space:
O(N)
Why:
Heap insertion and removal operations require logarithmic time for each report.
Edge-Case Checklist
 Empty graph
 One route
 Duplicate routes
 Disconnected locations
 Tie for most connected location
 Positive weighted routes
 Invalid zero or negative danger score
 Empty priority report list
Tests

Paste the result of your test run.

pytest -q

Result:

12 passed
Assistance & Sources

AI used? Yes

If yes, what did it help with?

Helped explain graph algorithms and heap queues.
Helped debug edge cases and improve code structure.
Helped improve README formatting and complexity explanations.

Other sources used:

Python documentation for heapq
Class lecture notes
ZyBooks examples