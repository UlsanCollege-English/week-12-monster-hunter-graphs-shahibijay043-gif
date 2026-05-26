"""Week 12: Monster Hunter Graphs.


This module provides:
- Unweighted graph construction
- Weighted graph construction
- Graph analytics
- Priority-based hunt ordering

Author:Bijay Shahi
"""

from __future__ import annotations

from collections import defaultdict
from typing import DefaultDict
import heapq


# =========================================================
# Type Aliases
# =========================================================

Graph = dict[str, list[str]]
WeightedGraph = dict[str, dict[str, int]]


# =========================================================
# Graph Construction Utilities
# =========================================================

def build_hunter_map(
    edges: list[tuple[str, str]],
) -> Graph:
    """
    Build an undirected adjacency-list graph.

    Args:
        edges:
            List of route pairs representing connections
            between monster hunting locations.

    Returns:
        A dictionary where:
        - keys are locations
        - values are sorted neighboring locations

    Example:
        >>> build_hunter_map([
        ...     ("Village", "Forest"),
        ...     ("Forest", "Castle")
        ... ])
        {
            'Forest': ['Castle', 'Village'],
            'Village': ['Forest'],
            'Castle': ['Forest']
        }
    """

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

        if not start.strip() or not end.strip():
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

    Each edge contains:
    - start location
    - end location
    - danger score

    Duplicate routes keep the LOWEST danger score.

    Args:
        edges:
            List of weighted route tuples.

    Returns:
        A weighted adjacency dictionary.

    Raises:
        TypeError:
            If danger score is not an integer.

        ValueError:
            If danger score is non-positive.
    """

    graph: DefaultDict[str, dict[str, int]]
    graph = defaultdict(dict)

    for start, end, danger_score in edges:

        if not isinstance(start, str):
            raise TypeError(
                "Start location must be a string."
            )

        if not isinstance(end, str):
            raise TypeError(
                "End location must be a string."
            )

        if not isinstance(danger_score, int):
            raise TypeError(
                "Danger score must be an integer."
            )

        if danger_score <= 0:
            raise ValueError(
                "Danger score must be positive."
            )

        if not start.strip() or not end.strip():
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


# =========================================================
# Graph Analytics
# =========================================================

def map_summary(
    graph: Graph,
) -> dict[str, int]:
    """
    Generate summary statistics for the graph.

    Args:
        graph:
            Hunter map adjacency list.

    Returns:
        Dictionary containing:
        - total locations
        - total routes
    """

    total_routes = (
        sum(len(neighbors)
        for neighbors in graph.values()) // 2
    )

    return {
        "locations": len(graph),
        "routes": total_routes,
    }


def most_connected_location(
    graph: Graph,
) -> str | None:
    """
    Find the location with the most neighbors.

    Ties are resolved alphabetically.

    Args:
        graph:
            Hunter map adjacency list.

    Returns:
        The most connected location or None
        if graph is empty.
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


# =========================================================
# Priority Queue Utilities
# =========================================================

def priority_hunt_order(
    reports: list[tuple[int, str]],
) -> list[str]:
    """
    Determine hunt order using a priority queue.

    Lower numeric value indicates
    HIGHER urgency.

    Args:
        reports:
            List of:
            (priority, location)

    Returns:
        Ordered list of locations.
    """

    if not reports:
        return []

    priority_queue = reports.copy()

    heapq.heapify(priority_queue)

    ordered_locations: list[str] = []

    while priority_queue:

        _, location = heapq.heappop(
            priority_queue
        )

        ordered_locations.append(location)

    return ordered_locations


# =========================================================
# Module Execution Guard
# =========================================================

if __name__ == "__main__":
    pass