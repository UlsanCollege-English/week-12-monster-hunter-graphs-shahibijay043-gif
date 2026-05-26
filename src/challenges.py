"""Week 12: Monster Hunter Graphs.

Rules:
- Standard library only.
- Use type hints.
- Keep public function docstrings.
- Run tests with: pytest -q
"""

from __future__ import annotations

from collections import defaultdict
import heapq


def build_hunter_map(
    edges: list[tuple[str, str]],
) -> dict[str, list[str]]:
    """Build an undirected adjacency list from route pairs."""

    graph: defaultdict[str, set[str]] = defaultdict(set)

    for start, end in edges:

        graph[start].add(end)
        graph[end].add(start)

    return {
        location: sorted(neighbors)
        for location, neighbors in graph.items()
    }


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]]
) -> dict[str, dict[str, int]]:
    """Build an undirected weighted graph from route triples."""

    graph: defaultdict[str, dict[str, int]]
    graph = defaultdict(dict)

    for start, end, weight in edges:

        if weight <= 0:
            raise ValueError(
                "Danger scores must be positive integers."
            )

        current_weight = graph[start].get(end)

        if (
            current_weight is None
            or weight < current_weight
        ):
            graph[start][end] = weight
            graph[end][start] = weight

    return {
        location: dict(sorted(neighbors.items()))
        for location, neighbors in graph.items()
    }


def map_summary(
    graph: dict[str, list[str]]
) -> dict[str, int]:
    """Return the number of locations and undirected routes."""

    unique_routes: set[frozenset[str]] = set()

    for start, neighbors in graph.items():

        for neighbor in neighbors:

            route = frozenset(
                {start, neighbor}
            )

            unique_routes.add(route)

    return {
        "locations": len(graph),
        "routes": len(unique_routes),
    }


def most_connected_location(
    graph: dict[str, list[str]]
) -> str | None:
    """Return the location with the most neighbors."""

    if not graph:
        return None

    max_connections = max(
        len(neighbors)
        for neighbors in graph.values()
    )

    candidates = [
        location
        for location, neighbors in graph.items()
        if len(neighbors) == max_connections
    ]

    return min(candidates)


def priority_hunt_order(
    reports: list[tuple[int, str]]
) -> list[str]:
    """Return monster sighting locations from most urgent to least urgent."""

    heap: list[tuple[int, str]] = []

    for priority, location in reports:

        heapq.heappush(
            heap,
            (priority, location),
        )

    ordered_locations: list[str] = []

    while heap:

        _, location = heapq.heappop(heap)

        ordered_locations.append(location)

    return ordered_locations