from fastapi import APIRouter

from app.api.log_route import LogRoute
from app.services.graph_filling import fill_graph, generate_quantity


router = APIRouter(route_class=LogRoute)
test_graph = fill_graph('hackathon_sirius_data.csv')

GRAPH = generate_quantity(test_graph)


@router.get(
    "/basic-line",
    name="",
)
def get_basic_line_chart():
    return {
        "xAxis": [
            "54 - 22",
            "22 - 28",
            "32 - 22",
            "48 - 54",
            "28 - 27",
            "34 - 32",
            "62 - 34",
            "10 - 34",
            "83 - 62",
            "2 - 10",
            "50 - 10"
        ],
        "series": [
            {
                "data": [26, 51, 37, 5, 17, 102, 42, 20, 36, 33, 17],
                "type": 'line'
            }
        ]
    }


@router.get(
    "/waterfall",
    name="",
)
def get_waterfall_chart():
    return {
        "xAxis": [
            'TonageLimit', 'TonageLimit', 'TonageLimit', 'TonageLimit', 'TonageLimit', 'TonageLimit', 'TonageLimit', 'TonageLimit', 'TonageLimit', 'TonageLimit',
        ],
        "series": [
            277320,
            2387478,
            2343746,
            12057,
            2527097,
            2344540,
            1319106,
            1888168,
            476521,
            143936,
            624441
        ]
    }


@router.get(
    "/pie",
    name="",
)
def get_pie_chart():
    return {
        "data": [
            {"value": 1111, "name": 'Max'},
            {"value": 444, "name": 'Marko'},
            {"value": 211, "name": 'Vladik'},
            {"value": 100, "name": 'Matvey'},
            {"value": 100, "name": 'Semka'}
        ]
    }
