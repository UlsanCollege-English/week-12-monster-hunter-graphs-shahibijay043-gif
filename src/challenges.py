"""Week 12: Monster Hunter Graphs."""

from __future__ import annotations

from collections import defaultdict
from typing import DefaultDict
import heapq


Graph = dict[str, list[str]]
WeightedGraph = dict[str, dict[str, int]]


def build_hunter_map(
    edges: list[tuple[str, str]],
) -> Graph:

    graph: DefaultDict[str, set[str]]
    graph = defaultdict(set)

    for start, end in edges:

        if not isinstance(start, str):
            raise TypeError(
                "Start location must be a string."
            )

        if not isinstance(end, str):
            raise TypeError(
                "End location must be a string."
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

    priority_queue = reports.copy()

    heapq.heapify(priority_queue)

    ordered_locations: list[str] = []

    while priority_queue:

        _, location = heapq.heappop(
            priority_queue
        )

        ordered_locations.append(location)

    return ordered_locations


if __name__ == "__main__":
    pass