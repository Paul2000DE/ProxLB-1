"""
Unit-testing static method update_node_resources in class Calculations
in calculations.py for edge cases where no nodes are available for balancing.
"""

__author__ = "Peter Dreuw <archandha>"
__copyright__ = "Copyright (C) 2026 Peter Dreuw (@archandha) for credativ GmbH"
__license__ = "GPL-3.0"


import pytest

from models.calculations import Calculations


def test_min_usage_with_empty_nodes() -> None:
    """
    Test the case where there are no nodes available (empty nodes dict).
    """
    method = "cpu"
    mode = "avg"
    proxlb_data = {
        "nodes": {},
        "meta": {"balancing": {}},
    }  # Simulate empty data

    proxlb_data_verify = proxlb_data.copy()

    Calculations.update_node_resources(proxlb_data)

    assert proxlb_data == proxlb_data_verify, "Proxlb data should not be modified when no nodes are available."


def test_min_usage_with_no_suitable_nodes() -> None:
    """
    Test the case where there are nodes, but none are suitable for balancing.
    """
    method = "cpu"
    mode = "avg"
    proxlb_data = {
        "nodes": {
            "node1": {"name": "node1", "cpu_avg_percent": 100, "maintenance": True},
            "node2": {"name": "node2", "cpu_avg_percent": 100, "maintenance": True},
        },
        "meta": {"balancing": {}},
    }  # Simulate nodes all in maintenance

    proxlb_data_verify = proxlb_data.copy()

    Calculations.update_node_resources(proxlb_data)

    assert proxlb_data == proxlb_data_verify, "Proxlb data should not be modified when no suitable nodes are available."
