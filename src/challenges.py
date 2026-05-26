"""Week 12: Monster Hunter Graphs.

Professional graph utility implementations using Python 3.11+.
"""

from __future__ import annotations

from collections import defaultdict
import heapq
from typing import DefaultDict



Graph = dict[str, list[str]]
WeightedGraph = dict[str, dict[str, int]]


def build_hunter_map(
    edges: list[tuple[str, str]],
) -> Graph:
    """
    Build an undirected adjacency list from route pairs.

    Args:
        edges: List of (start, end) route pairs.

    Returns:
        Sorted adjacency-list graph.
    """

    graph: DefaultDict[str, set[str]] = defaultdict(set)

    for start, end in edges:

        if not start or not end:
            raise ValueError(
                "Locations cannot be empty."
            )

        graph[start].add(end)
        graph[end].add(start)

    return {
        location: sorted(neighbors)
        for location, neighbors in sorted(graph.items())
    }


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]],
) -> WeightedGraph:
    """
    Build an undirected weighted graph.

    Keeps the smallest danger score if duplicate routes exist.
    """

    graph: DefaultDict[str, dict[str, int]]
    graph = defaultdict(dict)

    for start, end, danger_score in edges:

        if not isinstance(danger_score, int):
            raise TypeError(
                "Danger score must be an integer."
            )

        if danger_score <= 0:
            raise ValueError(
                "Danger score must be positive."
            )

        if not start or not end:
            raise ValueError(
                "Locations cannot be empty."
            )

        current_score = graph[start].get(end)

        if (
            current_score is None
            or danger_score < current_score
        ):
            graph[start][end] = danger_score
            graph[end][start] = danger_score

    return {
        location: dict(sorted(neighbors.items()))
        for location, neighbors in sorted(graph.items())
    }


def map_summary(
    graph: Graph,
) -> dict[str, int]:
    """
    Return summary statistics for the hunter map.
    """

    total_routes = sum(
        len(neighbors)
        for neighbors in graph.values()
    ) // 2

    return {
        "locations": len(graph),
        "routes": total_routes,
    }


def most_connected_location(
    graph: Graph,
) -> str | None:
    """
    Return the location with the most neighboring routes.

    Ties are resolved alphabetically.
    """

    if not graph:
        return None

    return min(
        graph,
        key=lambda location: (
            -len(graph[location]),
            location,
        ),
    )



def priority_hunt_order(
    reports: list[tuple[int, str]],
) -> list[str]:
    """
    Return locations ordered from highest urgency
    to lowest urgency.

    Lower numeric value = higher priority.
    """

    if not reports:
        return []

    priority_queue = reports[:]

    heapq.heapify(priority_queue)

    ordered_locations: list[str] = []

    while priority_queue:

        priority, location = heapq.heappop(
            priority_queue
        )

        ordered_locations.append(location)

    return ordered_locations



def main() -> None:
    """
    Example execution for GitHub Classroom
    autograder compatibility.
    """

    routes = [
        ("Village", "Forest"),
        ("Forest", "Castle"),
        ("Village", "Lake"),
        ("Lake", "Castle"),
    ]

    weighted_routes = [
        ("Village", "Forest", 3),
        ("Forest", "Castle", 5),
        ("Village", "Lake", 2),
        ("Lake", "Castle", 4),
    ]

    reports = [
        (1, "Castle"),
        (3, "Forest"),
        (2, "Lake"),
    ]

    graph = build_hunter_map(routes)

    weighted_graph = build_weighted_hunter_map(
        weighted_routes
    )

    print("Hunter Map:")
    print(graph)

    print("\nWeighted Hunter Map:")
    print(weighted_graph)

    print("\nMap Summary:")
    print(map_summary(graph))

    print("\nMost Connected Location:")
    print(
        most_connected_location(graph)
    )

    print("\nPriority Hunt Order:")
    print(
        priority_hunt_order(reports)
    )
def main():
    print("Monster Hunter Graphs Loaded")


if __name__ == "__main__":
    main()



    