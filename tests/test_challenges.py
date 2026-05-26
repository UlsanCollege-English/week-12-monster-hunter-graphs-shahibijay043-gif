"""Tests for challenges.py."""

from src.challenges import (
    build_hunter_map,
    build_weighted_hunter_map,
    map_summary,
    most_connected_location,
    priority_hunt_order,
)


def test_build_hunter_map():

    edges = [
        ("Village", "Forest"),
        ("Forest", "Castle"),
    ]

    expected = {
        "Castle": ["Forest"],
        "Forest": ["Castle", "Village"],
        "Village": ["Forest"],
    }

    assert build_hunter_map(edges) == expected


def test_build_weighted_hunter_map():

    edges = [
        ("Village", "Forest", 3),
        ("Forest", "Castle", 5),
    ]

    expected = {
        "Forest": {
            "Castle": 5,
            "Village": 3,
        },
        "Village": {
            "Forest": 3,
        },
        "Castle": {
            "Forest": 5,
        },
    }

    assert (
        build_weighted_hunter_map(edges)
        == expected
    )


def test_map_summary():

    graph = {
        "Village": ["Forest"],
        "Forest": ["Village", "Castle"],
        "Castle": ["Forest"],
    }

    expected = {
        "locations": 3,
        "routes": 2,
    }

    assert map_summary(graph) == expected


def test_most_connected_location():

    graph = {
        "Village": ["Forest"],
        "Forest": ["Village", "Castle"],
        "Castle": ["Forest"],
    }

    assert (
        most_connected_location(graph)
        == "Forest"
    )


def test_priority_hunt_order():

    reports = [
        (3, "Forest"),
        (1, "Castle"),
        (2, "Lake"),
    ]

    expected = [
        "Castle",
        "Lake",
        "Forest",
    ]

    assert (
        priority_hunt_order(reports)
        == expected
    )