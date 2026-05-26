from __future__ import annotations

from collections import defaultdict
import heapq


def build_hunter_map(
    edges: list[tuple[str, str]],
) -> dict[str, list[str]]:

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

    return dict(graph)


def map_summary(
    graph: dict[str, list[str]]
) -> dict[str, int]:

    routes = sum(
        len(neighbors)
        for neighbors in graph.values()
    ) // 2

    return {
        "locations": len(graph),
        "routes": routes,
    }


def most_connected_location(
    graph: dict[str, list[str]]
) -> str | None:

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
    reports: list[tuple[int, str]]
) -> list[str]:

    heap = reports[:]

    heapq.heapify(heap)

    ordered_locations = []

    while heap:

        _, location = heapq.heappop(heap)

        ordered_locations.append(location)

    return ordered_locations