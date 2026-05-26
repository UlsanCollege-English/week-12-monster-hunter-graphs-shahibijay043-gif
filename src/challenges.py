"""Week 12: Monster Hunter Graphs.

Professional graph utility implementations using Python 3.11+.
"""

from __future__ import annotations

from collections import defaultdict
import heapq


Graph = dict[str, list[str]]
WeightedGraph = dict[str, dict[str, int]]


def build_hunter_map(
    edges: list[tuple[str, str]],
) -> Graph:
    """Build an undirected adjacency list from route pairs."""

    graph: defaultdict[str, set[str]] = defaultdict(set)

    for start, end in edges:

        graph[start].add(end)
        graph[end].add(start)

    return {
        location: sorted(neighbors)
        for location, neighbors in sorted(graph.items())
    }


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]],
) -> WeightedGraph:
    """Build an undirected weighted graph from route triples."""

    graph: defaultdict[str, dict[str, int]]
    graph = defaultdict(dict)

    for start, end, danger_score in edges:

        if not isinstance(danger_score, int):
            raise ValueError(
                "Danger score must be an integer."
            )

        if danger_score <= 0:
            raise ValueError(
                "Danger score must be positive."
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
    """Return summary statistics for the hunter map."""

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
    """Return the location with the most neighboring routes."""

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
    """Return locations ordered from highest urgency to lowest."""

    priority_queue = reports[:]

    heapq.heapify(priority_queue)

    ordered_locations: list[str] = []

    while priority_queue:

        _, location = heapq.heappop(
            priority_queue
        )

        ordered_locations.append(location)

    return ordered_locations